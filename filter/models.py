from django.db import models
from django_resized import ResizedImageField
from taggit.managers import TaggableManager


def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=140)
    image = ResizedImageField(size=[250, 250],
                              upload_to=upload_location,
                              blank=True,
                              null=True)

    qr = ResizedImageField(size=[250, 250],
                           upload_to=upload_location,
                           blank=True,
                           null=True)
    date = models.DateField()
    tags = TaggableManager()

    def __str__(self):
        return self.title

