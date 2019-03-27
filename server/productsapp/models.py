from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank = True,
        null = True, 
        default = 'empty', 
        )

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(
        max_length=255,
        blank = True,
        null = True,
        )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name    


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
    )

    type = models.ForeignKey(
        Type,
        on_delete = models.CASCADE,
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default = 0,
        )

    discount = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        default = 0,
    )