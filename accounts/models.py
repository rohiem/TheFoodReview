from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField( upload_to="profile", default="profile/profile.jpg")
    slug=models.SlugField(blank=True,null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
