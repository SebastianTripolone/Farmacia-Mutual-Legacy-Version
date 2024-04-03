from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
import os

class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    STATUS = (
        ('cliente', 'cliente'),
        ('Auxiliar', 'Auxiliar'),
        ('Administrativo', 'Administrativo'),
        ('Farmaceutico', 'Farmaceutico'),
        ('Medico', 'Medico'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='Empleado')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to)

    def __str__(self):
        return self.username

# Create your models here.
