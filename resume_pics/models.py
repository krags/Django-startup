from django.db import models
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media')

class Photo(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    width = models.IntegerField(default=200)
    # height = models.IntegerField(default=25)
    image = models.ImageField(upload_to="pictures")
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ["timestamp"]
    #     verbose_name = 'Photo'
