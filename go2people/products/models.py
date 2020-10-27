from django.db import models
from pathlib import Path


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='company_logo',default='static/no-image.png')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='product_pics',default='static/no-image.png')
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company,related_name='company',on_delete=models.CASCADE)
    categories = (('I Category', '1'), ('II Category', '2'), ('III Category', '3'),
                  ('IV Category', '4'), ('V Category', '5'), ('VI Category', '6'))
    category = models.CharField(max_length=256, choices=categories)
    schooltypes = (('praktijkonderwijs','praktijkonderwijs'), ('vmbo','vmbo'), ('mbo','mbo'),
                   ('hbo','hbo'), ('opleidingsbedrijf','opleidingsbedrijf'))
    schooltype= models.CharField(max_length=256, choices=schooltypes)
    price = models.DecimalField(decimal_places=2,default=0,max_digits=8)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
