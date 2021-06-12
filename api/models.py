from django.db import models

# Create your models here.

class Picture(models.Model):
    title=models.CharField(max_length=100)
    p_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Home(models.Model):
    title=models.CharField(max_length=100)
    descript = models.CharField(max_length=500)

    def __str__(self):
        return self.title