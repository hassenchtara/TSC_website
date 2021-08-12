from django.db import models

class slide(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    link = models.CharField(max_length=100)

class produit(models.Model):
    Category = models.TextField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo_main = models.ImageField()
    photo_1 = models.ImageField(blank=True)
    photo_2 = models.ImageField(blank=True)
    photo_3 = models.ImageField(blank=True)
    photo_4 = models.ImageField(blank=True)
    photo_5 = models.ImageField(blank=True)
    photo_6 = models.ImageField(blank=True)
    photo_7 = models.ImageField(blank=True)
    photo_8 = models.ImageField(blank=True)
    photo_9 = models.ImageField(blank=True)
    Accueil = models.BooleanField(default=False)
