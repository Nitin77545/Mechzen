from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings 


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g. "45–60 mins"
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="mechanics/", null=True, blank=True)
    rating = models.FloatField(default=5.0)
    vehicle_number = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    eta_minutes = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class Profile(models.Model):
    from django.conf import settings  # ✅ import this
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # ✅ use custom user
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)

    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # only when user is created
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
