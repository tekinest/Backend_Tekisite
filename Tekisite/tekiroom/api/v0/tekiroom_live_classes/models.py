from django.db import models

# Create your models here.


class TekiroomLiveClass(models.Model):
    name = models.CharField(max_length=999)
    url = models.URLField(default="www.tekiroom.tekisite.com/live")
    # slug = models.SlugField()
    def __str__(self):
        return self.name
     
