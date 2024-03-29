from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(f'{self.name}')


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model: str = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.fields.FloatField(blank=True, null=True)

    def __str__(self):
        return str(f'{self.model}')
