from django.db import models
import datetime as dt
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
      return self.name

class Photo(models.Model):
  category = models.ForeignKey( Category, on_delete=models.SET_NULL, null=True, blank=True )
  image = CloudinaryField('image')
  description= models.TextField()

  def __str__(self):
      return self.description
