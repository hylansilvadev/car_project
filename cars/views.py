from django.shortcuts import render

from cars.models import Car, Brand

# Create your views here.


def car_view(request):
    cars = Car.objects.filter(brand__name='Volkswagen')
    print(cars)
    return render(
        request, 
        'cars.html', 
        {'cars': cars}
        )
