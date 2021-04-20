from django.core.signals import post_delete, post_init, post_save
from django.dispatch import receiver

from tasks.models import Task, TimeLog


@receiver([post_save, post_delete], sender=Task)
def update_project_last_modified(sender, instance, **kwargs):
    instance.project.last_modified = timezone.now()
    instance.project.save()


@receiver([post_init], sender=TimeLog, dispatch_uid="timelog_post_init")
def timelog_post_init(sender, instance, **kwargs):
    if instance.pk:
        for field in instance.init_track_fields:
            setattr(instance, f"_original_{field}", getattr(instance, field))


# signals.post_save.connect(update_project_last_modified, sender=Task)
# signals.post_delete.connect(update_project_last_modified, sender=Task)
