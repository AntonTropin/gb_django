from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True, 
        default = 'empty', 
        )

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
        )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name   


class ProductPhoto(models.Model):

    image = models.ImageField(
        upload_to = 'products',
        null = True,
        blank = True,
    ) 

    description = models.TextField(
        blank = True,
        null = False,
    )

    def __str__(self):
        return self.description


class Colour(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name

class Diagonal(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name

class Memory(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name

class Processor(models.Model):

    name = models.TextField(
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Features(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Storage(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Band(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class CaseMaterial(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Connectivity(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Year(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Description(models.Model):

    name = models.TextField(
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    short_description = models.CharField(
        max_length = 255,
        blank = True,
        null = True,
    )

    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
    )

    type = models.ForeignKey(
        Type,
        on_delete = models.CASCADE,
    )

    productphoto = models.ForeignKey(
        ProductPhoto,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    colour = models.ForeignKey(
        Colour,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    diagonal = models.ForeignKey(
        Diagonal,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    memory = models.ForeignKey(
        Memory,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    processor = models.ForeignKey(
        Processor,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    features = models.ForeignKey(
        Features,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    storage = models.ForeignKey(
        Storage,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    band = models.ForeignKey(
        Band,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    casematerial = models.ForeignKey(
        CaseMaterial,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    connectivity = models.ForeignKey(
        Connectivity,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    year = models.ForeignKey(
        Year,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    description = models.ForeignKey(
        Description,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    price = models.DecimalField(
        max_digits = 12,
        decimal_places = 2,
        default = 0,
        )

    discount = models.DecimalField(
        max_digits = 2,
        decimal_places = 2,
        default = 0,
        null = True,
    )

    created = models.DateTimeField(
        auto_now_add = True,
    )

    modified = models.DateTimeField(
        auto_now = True,
    )

    def __str__(self):
        return f'{self.name} {self.short_description}' 

