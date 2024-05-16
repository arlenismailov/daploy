from django.db import models


class CarorSpareparts(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


# сатуучуга
class Brand(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    img = models.ImageField(upload_to='image/', null=True, blank=True)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, related_name='reviews', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='reviews', on_delete=models.CASCADE)
    year = models.IntegerField(default=2000)
    mileage = models.IntegerField(default=0)
    body_color = models.CharField(max_length=20)
    interior_color = models.CharField(max_length=20)
    engine = models.CharField(max_length=40)
    transmission = models.CharField(max_length=40)
    place = models.CharField(max_length=32, default='Bishkek')


class CarBet(models.Model):
    number = models.IntegerField(default=0)
    total_number = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    start_date = models.DateTimeField
    end_date = models.DateField()