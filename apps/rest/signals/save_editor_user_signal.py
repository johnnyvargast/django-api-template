from apps.rest.middleware.request_middleware import get_current_user


def pre_save_save_editor_user(sender, instance, **kwargs):
    try:
        instance.old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        instance.old_instance = instance


def post_save_save_editor_user(sender, instance, created, **kwargs):
    current_user = get_current_user()

    # archive data
    data_to_archive = {}

    if created:
        if instance.is_archived:
            data_to_archive.update({
                "archived_by": current_user,
                "archived_at": instance.updated_at,
            })

        sender.objects.update(
            created_by=current_user,
            updated_by=current_user,
            **data_to_archive)
    else:
        if instance.is_archived and not instance.old_instance.is_archived:
            data_to_archive.update({
                "archived_by": current_user,
                "archived_at": instance.updated_at,
            })
        elif not instance.is_archived and instance.old_instance.is_archived:
            data_to_archive.update({
                "archived_by": None,
                "archived_at": None,
            })

        sender.objects.update(
            updated_by=current_user,
            **data_to_archive)
