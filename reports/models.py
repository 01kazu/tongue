from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# User = settings.AUTH_USER_MODEL
# Create your models here.

class Report(models.Model):
    user = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    post = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("reports:all_posts_detail", kwargs={'pk': self.pk})

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     matric_number = models.CharField(max_length=17)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


