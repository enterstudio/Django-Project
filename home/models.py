from django.db import models
from taggit.managers import TaggableManager

def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to=upload_location,
                              blank=True,
                              null=True)
    qr = models.ImageField(upload_to=upload_location,
                           blank=True,
                           null=True)
    date = models.DateField()
    tags = TaggableManager()

    def __str__(self):
        return self.title

