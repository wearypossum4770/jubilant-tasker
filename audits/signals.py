from django.db.models.signals import post_init


def timelog_post_init(sender, instance, **kwargs):
    if instance.pk:
        for field in instance.init_track_fields:
            setattr(instance, "_original_%s" % field, getattr(instance, field))
