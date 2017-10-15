from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class School(models.Model):
    name =models.CharField(max_length=264,unique=True)
    principal =models.CharField(max_length=264)
    location =models.CharField(max_length=264)

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Student(models.Model):
    name =models.CharField(max_length=264)
    age =models.PositiveIntegerField()
    school =models.ForeignKey(School,related_name='student')

    def __str__(self):
        return self.name


