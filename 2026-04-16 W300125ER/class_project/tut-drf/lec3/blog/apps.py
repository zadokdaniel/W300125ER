from django.apps import AppConfig

from django.dispatch import receiver
from django.db.models.signals import post_save


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    @receiver(post_save, sender='auth.User')
    def perform_add_user_to_default_group(sender, instance, created, **kwargs):
        if not created:
            return

        from django.contrib.auth.models import  Group

        if created:
            group, _ = Group.objects.get_or_create(name="users")
            instance.groups.add(group)
            instance.save()

            print(f'User {instance.username} added to group {group.name}')
