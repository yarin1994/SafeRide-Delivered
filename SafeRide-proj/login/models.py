from django.db import models
from django.contrib.auth.models import User , AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


    

class Scooter(models.Model):
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    serial_number   = models.CharField(max_length=5)

    BIRD = 'bird'
    WIND = 'wind'
    LIME = 'lime'
    BRAND_CHOICES = [
        (BIRD, 'bird'),
        (WIND, 'wind'),
        (LIME, 'lime')
    ]
    brand = models.CharField(
        max_length=4,
        choices=BRAND_CHOICES,
    
    )

    
    TELAVIV = 'Tel Aviv'
    RAMATGAN = 'Ramat Gan'
    GIVATAYIM = 'Givatayim'
    CITY_CHOICES = [
        (TELAVIV, 'Tel Aviv'),
        (RAMATGAN, 'Ramat Gan'),
        (GIVATAYIM, 'Givatayim')
    ]
    city = models.CharField(
        max_length=10,
        choices=CITY_CHOICES,
        default=TELAVIV,
    )
    
    helmet          = models.BooleanField(default=False)
    
    NEW = 'new'
    USED = 'used'
    REPAIR = 'repair'
    CONDITION_CHOICES = [
        (NEW, 'new'),
        (USED, 'used'),
        (REPAIR, 'repair')
    ]
    status = models.CharField(
        max_length=6,
        choices=CONDITION_CHOICES,
    
    )
    battery = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    

    def __str__(self):
        return self.serial_number



