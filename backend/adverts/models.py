from backend.base.models import User
from django.db import models


class CreatedUpdatedAbstract(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Address(CreatedUpdatedAbstract):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    zip_code = models.CharField(max_length=9)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=128)
    uf = models.CharField(max_length=2)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.zip_code

    class Meta:
        ordering = ("created_at",)


class Advert(CreatedUpdatedAbstract):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    description = models.TextField()
    opened = models.BooleanField(default=True)

    class Meta:
        ordering = ("created_at",)
