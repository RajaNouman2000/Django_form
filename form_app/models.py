from django.db import models

# Create your models here.


class Registeration_form(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    posts = (('Manager', 'Manager'), ('Cashier',
             'Cashier'), ('Operator', 'Operator'))
    field = models.CharField(choices=posts, max_length=20)
