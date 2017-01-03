from django.db import models

# Create your models here.

class Pizza(models.Model):
    """Pizza model"""
    name = models.CharField(max_length=30)

    def __str__(self):
        """Text string representing model"""
        return self.name


class Topping(models.Model):
    """Topping model"""
    pizza = models.ForeignKey(Pizza)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        """Text string representing model"""
        return self.name
