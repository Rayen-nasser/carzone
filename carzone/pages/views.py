from django.core.paginator import Paginator
from django.db.models import Max, Min
from django.shortcuts import render
from .models import Team
from cars.models import Car

# Utility function for pagination
def paginate_items(request, items, num_items=4):
    paginator = Paginator(items, num_items)
    page_number = request.GET.get('page')
    paginated_items = paginator.get_page(page_number)
    return paginated_items

# Home view
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_date')
    latest_cars = Car.objects.order_by('-created_date')

    # Get distinct values for model, year, body_style, and city
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()

    # Get maximum and minimum price
    price_range = Car.objects.aggregate(max_price=Max('price'), min_price=Min('price'))

    context = {
        "teams": paginate_items(request, teams),
        "featured_cars": featured_cars,
        "latest_cars": latest_cars,
        "model_search": model_search,
        "year_search": year_search,
        "body_style_search": body_style_search,
        "city_search": city_search,
        'min_price': price_range['min_price'],
        'max_price': price_range['max_price'],
    }
    return render(request, 'pages/home.html', context)

# About view
def about(request):
    teams = Team.objects.all()
    context = {
        "teams": paginate_items(request, teams)
    }
    return render(request, 'pages/about.html', context)

# Services view
def services(request):
    return render(request, 'pages/services.html')

# Contact view
def contact(request):
    return render(request, 'pages/contact.html')
