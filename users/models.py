from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    ImageField,
    IntegerChoices,
    ManyToManyField,
    Model,
    OneToOneField,
    PositiveSmallIntegerField,
)
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    return f"user_{instance.user.id}/profile_pics/{filename}"


class Role(Model):
    class UserType(IntegerChoices):
        REGULAR = 0, _("Regular User")
        STUDENT = 1, _("Student")
        TEACHER = 2, _("Teacher")
        SECRETARY = 3, _("Secretary")
        SUPERVISOR = 4, _("Supervisor")
        ADMIN = 5, _("Administrator")

    user_type = PositiveSmallIntegerField(
        choices=UserType.choices, default=UserType.REGULAR, primary_key=True
    )


class User(AbstractUser):
    roles = ManyToManyField(Role)
    middle_name = CharField(max_length=30, blank=True)
    date_of_birth = DateField(null=True, blank=True)

    @property
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def read(self):
        self.last_read_date = timezone.now()
        self.save()

    def unread_messages(self):
        return Message.objects.filter(created_at__gt=self.last_read_date) \
                              .count()
class Profile(Model):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    user = OneToOneField(get_user_model(), on_delete=SET_NULL, null=True)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)
    is_public = BooleanField(default=False)
    is_active = BooleanField(default=True)
    image = ImageField(default="default.webp", upload_to=user_directory_path)
    # @cached_property
    # def friends(self):
    #     pass


#  have rust task using celery or golang task to convert image files to webp.
