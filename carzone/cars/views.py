from django.shortcuts import render, get_object_or_404

from .models import Car
from pages.views import paginate_items


def cars(request):
    cars_list = Car.objects.all()
    context = {
        "cars": paginate_items(request, cars_list),
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context)
