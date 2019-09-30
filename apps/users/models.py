"""Modelo Usuarios"""

# Django
from django.db import models
from django.contrib.auth.models import User

from apps.core import choices


class Profile(models.Model):
    """Modelo Perfil"""
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name_company = models.CharField(max_length=80, default='')
    nit = models.CharField(max_length=20, default='')
    token = models.CharField(max_length=32, default='')
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    rol = models.CharField(max_length=20, blank=False, choices=choices.ROL_USER)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateField(auto_now=True)

    def __str__(self):
        return self.name_company
