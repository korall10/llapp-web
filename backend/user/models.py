import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class PermissionGroups(models.Model):
    name = models.CharField(max_length=512, unique=True,
                            verbose_name='İzin Grubu adı')
    key = models.CharField(max_length=512, unique=True,
                           verbose_name='İzin Grubu adı', null=True, blank=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    group = models.ForeignKey(
        PermissionGroups, on_delete=models.CASCADE, blank=True, null=True, related_name="permissions")
    name = models.CharField(max_length=512, verbose_name='İzin adı')
    key = models.CharField(max_length=512, unique=True,
                           verbose_name='İzin adı')
    description = models.TextField()

    def __str__(self):
        return self.key


class Role(models.Model):
    name = models.CharField(max_length=512, unique=True,
                            verbose_name='Rol adı')
    key = models.CharField(max_length=512, unique=True,
                           verbose_name='Rol adı', null=True, blank=True)
    permissions = models.ManyToManyField(
        Permission, related_name="permissions")

    def __str__(self):
        return self.name


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)
    address = models.TextField(null=True)
    phone = models.BigIntegerField(null=True)
    tc_no = models.BigIntegerField(null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    force_password_change = models.BooleanField(default=True)
    slug = models.CharField(max_length=256, blank=True, null=True)
    login_counter = models.IntegerField(default=0)
    login_block = models.DateTimeField(auto_now_add=True, null=True)
