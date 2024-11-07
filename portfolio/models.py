from django.db import models
from django.db.models.fields import CharField, URLField, DateField
from django.db.models.fields.files import ImageField
import datetime



class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
    
class Icon(models.Model):
    image = ImageField(upload_to='portfolio/images/')
    title = CharField(max_length=50, default='Sin título')
    
class Education(models.Model):
    image = ImageField(upload_to='portfolio/images/')
    title = CharField(max_length=50)
    description = CharField(max_length=150)
    date_ini = DateField(default=datetime.date.today, null=True, blank=True)
    date_fin = DateField(default=datetime.date.today, null=True, blank=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    msj = models.TextField(default='Hola, Maribel, vi tu portafolio y deseo contactarme contigo')

    def __str__(self):
        return self.name