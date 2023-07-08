from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.apps.models import App, Task
 
 
@receiver(post_save, sender=App)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(app=instance)


@receiver(post_save, sender=Task)
def create_profile(sender, instance, created, **kwargs):
    if instance.is_completed:
        instance.user.points += instance.app.points
        instance.user.save()