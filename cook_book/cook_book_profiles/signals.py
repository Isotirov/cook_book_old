from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from cook_book.cook_book_profiles.models import CookBookUserProfile


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_after_user_registration(created, instance, **kwargs):
    if created:
        profile = CookBookUserProfile(
            user=instance
        )
        profile.save()


@receiver(pre_save, sender=CookBookUserProfile)
def check_profile_completion(instance, **kwargs):
    first_name = 'Нов'
    last_name = 'Профил'

    if instance.image and not instance.first_name == first_name and not instance.last_name == last_name:
        instance.is_complete = True
    else:
        instance.is_complete = False
