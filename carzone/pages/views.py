from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Team
from cars.models import Car

def paginate_items(request, items, num_items=4):
    paginator = Paginator(items, num_items)
    page_number = request.GET.get('page')
    paginated_items = paginator.get_page(page_number)
    return paginated_items

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_date')
    latest_cars = Car.objects.order_by('-created_date')
    context = {
        "teams": paginate_items(request, teams),
        "featured_cars": featured_cars,
        "latest_cars": latest_cars
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Team.objects.all()
    context = {
        "teams": paginate_items(request, teams)
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

