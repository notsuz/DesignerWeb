from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    caption=models.CharField(max_length=200)
     
    def __str__(self):
        return self.title
    
class UiDesign(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    caption=models.CharField(max_length=200)
     
    def __str__(self):
        return self.title