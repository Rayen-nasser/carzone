from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)


        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        print("logout")
        auth.logout(request)
        # messages.success(request, 'You are successfully logged out.')
        return redirect('home')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('register')
            else:
                # Create user
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                email=email, password=password)

                # Log in the user after successful registration
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)

                messages.success(request, 'You are registered successfully.')
                return redirect('dashboard')  # Redirect to dashboard after successful registration and login
        else:
            messages.error(request, "Passwords don't match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
