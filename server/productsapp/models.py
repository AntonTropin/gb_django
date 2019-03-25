from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=255, 
        blank=True,
        null=False,
        )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=255, 
        blank=True,
        null=False,
        )

    def __str__(self):
        return self.name


# class Type(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name    

# class Colour(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Diagonal(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Memory(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Processor(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Features(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Graphics(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Storage(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Band(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Case(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Connectivity(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Year(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Description(models.Model):
#     name = models.TextField()

#     def __str__(self):
#         return self.name

# class Photo(models.Model):
#     name = models.ImageField(upload_to=​'products_images'​, blank=​True​)

#     def __str__(self):
#         return self.name