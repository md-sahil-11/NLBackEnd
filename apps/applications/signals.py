from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.applications.models import Task
 
 
@receiver(post_save, sender=Task)
def update_user_points(sender, instance, created, **kwargs):
    if created:
        instance.user.points += instance.app.points
        instance.user.save()