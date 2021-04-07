def update_project_last_modified(sender, instance, **kwargs):
    instance.project.last_modified = timezone.now()
    instance.project.save()

signals.post_save.connect(update_project_last_modified, sender=Task)
signals.post_delete.connect(update_project_last_modified, sender=Task)
