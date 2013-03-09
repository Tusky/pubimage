from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

YES_OR_NO = (
    (1, 'Yes'),
    (0, 'No')
)

class images(models.Model):
    name        = models.CharField("Name", max_length=255)
    description = models.TextField("Description", blank=True)
    uploaded_on = models.DateField("Uploaded on", auto_now_add=True)
    image       = models.ImageField("Image File", upload_to="temp/")
    public      = models.IntegerField("Do you want this image to be publicly avaliable?", choices=YES_OR_NO, default=1)
    views       = models.IntegerField("Number of views", default=0)
    likes       = models.IntegerField("Likes", default=0)
    dislikes    = models.IntegerField("Dislikes", default=0)
    uploaded_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Image'

admin.site.register(images)