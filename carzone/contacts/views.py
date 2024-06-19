from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from .models import Contact
from django.contrib.auth.models import User
import logging

from carzone import settings

logger = logging.getLogger(__name__)

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        user_id = request.POST.get('user_id')
        car_title = request.POST.get('car_title')
        customer_need = request.POST.get('customer_need')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        message = request.POST.get('message')

        # Ensure all required fields are provided
        required_fields = ['car_id', 'user_id', 'car_title', 'customer_need', 'email', 'phone', 'message']
        if not all(request.POST.get(field) for field in required_fields):
            messages.error(request, 'Please fill out all required fields.')
            return redirect('some_form_page')  # Replace with your form page URL

        # Check if the user has already made an inquiry about this car
        if Contact.objects.filter(car_id=car_id, user_id=user_id).exists():
            messages.error(request, f'You have already made an inquiry about this car ({car_title}). Please wait until we get back to you.')
            return redirect("/cars/" + car_id)

        # Create a new contact record
        try:
            contact = Contact.objects.create(
                car_id=car_id,
                user_id=user_id,
                customer_need=customer_need,
                car_title=car_title,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                city=city,
                state=state,
                message=message
            )

            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email
            send_mail(
                "New Car Inquiry",
                f'Inquiry Message:\n\n{message}\n\nCustomer Need: {customer_need}\n\nContact Details:\nName: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}\nCity: {city}\nState: {state}',
                settings.EMAIL_HOST_USER,
                [admin_email],
                fail_silently=False,
            )
            messages.success(request, 'Your request has been submitted. We will get back to you shortly.')
            return redirect(reverse('car_detail', args=[car_id]))  # Replace 'car_detail' with your actual URL name
        except Exception as e:
            logger.error(f'An error occurred: {e}')
            messages.error(request, f'An error occurred: {e}')
            return redirect('/cars')

    return render(request, 'home')  # Replace 'inquiry_form.html' with your actual template path
