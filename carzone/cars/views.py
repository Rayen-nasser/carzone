from django.shortcuts import render, get_object_or_404
from .models import Car
from django.db.models import Max, Min
from pages.views import paginate_items

def get_search_options():
    """Helper function to get distinct search options."""
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    return model_search, year_search, body_style_search, city_search

def get_price_range():
    """Helper function to get minimum and maximum prices."""
    price_range = Car.objects.aggregate(max_price=Max('price'), min_price=Min('price'))
    return price_range['min_price'], price_range['max_price']

def cars(request):
    cars_list = Car.objects.order_by('-created_date')

    # Apply filters based on search criteria
    keyword = request.GET.get('keyword')
    if keyword:
        cars_list = cars_list.filter(description__icontains=keyword)

    model = request.GET.get('model')
    if model:
        cars_list = cars_list.filter(model__iexact=model)

    year = request.GET.get('year')
    if year:
        cars_list = cars_list.filter(year__iexact=year)

    body_style = request.GET.get('body_style')
    if body_style:
        cars_list = cars_list.filter(body_style__iexact=body_style)

    city = request.GET.get('location')
    if city:
        cars_list = cars_list.filter(city__iexact=city)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        cars_list = cars_list.filter(price__gte=min_price, price__lte=max_price)

    model_search, year_search, body_style_search, city_search = get_search_options()
    min_price, max_price = get_price_range()

    context = {
        "cars": paginate_items(request, cars_list),
        "model_search": model_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
        "city_search": city_search,
        "min_price": min_price,
        "max_price": max_price,
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context)


def search(request):
    cars_list = Car.objects.order_by('-created_date')

    # Filter by keyword
    keyword = request.GET.get('keyword')
    if keyword:
        cars_list = cars_list.filter(description__icontains=keyword)

    # Filter by model
    model = request.GET.get('model')
    if model:
        cars_list = cars_list.filter(model__iexact=model)

    # Filter by city
    city = request.GET.get('location')
    if city:
        cars_list = cars_list.filter(city__iexact=city)

    # Filter by transmission
    transmission = request.GET.get('transmission')
    if transmission:
        cars_list = cars_list.filter(transmission__iexact=transmission)

    # Filter by year
    year = request.GET.get('year')
    if year:
        cars_list = cars_list.filter(year__iexact=year)

    # Filter by body style
    body_style = request.GET.get('body_style')
    if body_style:
        cars_list = cars_list.filter(body_style__iexact=body_style)

    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        cars_list = cars_list.filter(price__gte=min_price, price__lte=max_price)

    model_search, year_search, body_style_search, city_search = get_search_options()

    context = {
        "cars": cars_list,
        "model_search": model_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
        "city_search": city_search,

    }
    return render(request, 'cars/search.html', context)
