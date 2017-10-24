from django.db import models
from basic_app.models import School
from django.core.urlresolvers import reverse

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=264)
    age =models.PositiveIntegerField()
    school =models.ForeignKey(School,related_name='student')

    def get_absolute_url(self):
        return reverse("basic_app:list")

    def __str__(self):
        return self.name