from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + 'Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Requests(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.profile.user.username



