from django.db.models.signals import post_save
from .models import MyUser, UserPosition
from django.dispatch import receiver

@receiver( post_save, sender=MyUser )
def create_position( sender, instance, created, **kwargs ):
    if created:
        UserPosition.objects.create( user=instance )

@receiver( post_save, sender=MyUser )
def save_position( sender, instance, **kwargs):
    instance.userposition.save()