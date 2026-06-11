from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=50)
    image=CloudinaryField('images')
    caption=models.CharField(max_length=200)
    description=models.TextField(null=True)
     
    def __str__(self):
        return self.title
    
class ProjectImages(models.Model):
    image=CloudinaryField('images')
    project=models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='images')
    
class UiDesign(models.Model):
    title=models.CharField(max_length=50)
    image=CloudinaryField('images')
    caption=models.CharField(max_length=200)
     
    def __str__(self):
        return self.title
    
class UiImages(models.Model):
    image=CloudinaryField('images')
    project=models.ForeignKey(UiDesign, on_delete=models.CASCADE, related_name='images')
    
class Logo(models.Model):
    title=models.CharField(max_length=50)
    image=CloudinaryField('images')
    caption=models.CharField(max_length=200)
     
    def __str__(self):
        return self.title


class Poster(models.Model):
    title=models.CharField(max_length=50)
    image=CloudinaryField('images')
    caption=models.CharField(max_length=200)
     
    def __str__(self):
        return self.title