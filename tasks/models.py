from datetime import date
from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import (
    CASCADE,
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    FileField,
    ForeignKey,
    ManyToManyField,
    Model,
    PositiveIntegerField,
    TextField,
    UUIDField,
)
from django.utils import timezone

User = get_user_model()

# idempotent_key
def get_attachment_upload_dir(instance, filename):
    """Determine upload dir for task attachment files."""
    return f"{tasks}/{attachments}/{str(instance.task.id)}/{filename}"
class Project(Model):
    name = CharField(max_length=200)
    last_modified = DateTimeField(auto_now=True)


class Task(Model):
    project = ForeignKey(Project, on_delete=SET_NULL, null=True)
    external_id = UUIDField(default=uuid4, primary_key=False)
    title = CharField(max_length=80)
    content = CharField(max_length=100)
    date_modified = DateTimeField(auto_now=True)
    date_created = DateTimeField(auto_now_add=True)
    date_due = DateField(null=True, blank=True)
    date_completed = DateTimeField(null=True, blank=True)
    completed = BooleanField(default=False)
    created_by = ForeignKey(
        User,
        related_name="todo_created_by",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    assigned_to = ForeignKey(
        User,
        related_name="todo_assigned_to",
        blank=True,
        null=True,
        on_delete=CASCADE,
    )
    note = TextField(blank=True, null=True)
    priority = PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.completed:
            self.date_completed = timezone.now()
        super().save()

    @property
    def is_due(self, *args, **kwargs):
        return date.today() == self.date_due

    @property
    def is_overdue(self, *args, **kwargs):
        return date.today() > self.date_due


class Comment(Model):
    author = ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    task = ForeignKey(Task, on_delete=CASCADE)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)
    # email_from = CharField(max_length=320, blank=True, null=True)
    # email_message_id = CharField(max_length=255, blank=True, null=True)
    body = TextField(blank=True)

    def __str__(self):
        return f"Author:{self.author} content:{self.body[0:50]}"


class Attachment(Model):
    task = ForeignKey(Task, on_delete=CASCADE)
    added_by = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    timestamp = DateTimeField(default=timezone.now)
    file_location = FileField(upload_to=get_attachment_upload_dir, max_length=255)

    def __str__(self):
        return f"{self.task.id} - {self.file.name}"

    def filename(self):
        return Path(self.file_location.name).name

    def extension(self):
        return self.filename.suffix


class Note(Model):
    note = TextField()


class TimeLog(Model):
    time_spent = DecimalField(max_digits=4, decimal_places=2)
    notes = ManyToManyField(Note, blank=True)

    @property
    def init_track_fields(self):
        return ("time_spent",)

    def add_track_save_note(self):
        field_track = {}
        for field in self.init_track_fields:
            value = getattr(self, field)
            orig_value = getattr(self, f"_original_{field}")
            if value != orig_value:
                field_track[field] = [orig_value, value]

        if field_track:
            note_str = "The following fields were updated:<br /><br />"
            for k, v in field_track.iteritems():
                note_str += f"<b>{k}:</b> <i>{v[0]}</i><b>&rarr;</b> {v[1]}<br />"
            note = Note.objects.create(note=note_str)
            self.notes.add(note)

    def save(self, *args, **kwargs):
        if self.pk:
            self.add_track_save_note()
        super().save(*args, **kwargs)
