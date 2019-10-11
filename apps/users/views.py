from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from apps.users.models import Profile 
from apps.home.mixins import DashboardLoginRequiredMixin

# Exections
from django.db.utils import IntegrityError


# class UserDetailView(DashboardLoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'usuarios/user_detail.html'

#     def get_success_url(self):
#         return reverse("dashboard")


def loginView(request):
    nit = name_company = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(request, username=username, password=password)
        profile_obj = Profile.objects.get(user=user.id)
        nit = profile_obj.nit if profile_obj else nit
        name_company = profile_obj.name_company if profile_obj else name_company
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error':'Usuario o Password incorrectos'})
    return render(request, 'users/login.html')


def logoutView(request):
    logout(request)
    return redirect('login')

# def signupView(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         password_confirmation = request.POST['password_confirmation']
        
#         if password != password_confirmation:
#             return render(request, 'users/signup.html', {'error':'Password no coinciden'})
#         try: 
#             user = User.objects.create_user(email=email, password=password)
#         except IntegrityError:
#             return render(request, 'users/signup.html', {'error':'Usuario ya existe'})
#         user.first_name = request.POST['first_name']
#         user.last_name = request.POST['last_name']
#         user.email = request.POST['email']
#         user.save()
#         perfil = Perfil(usuraio=user)
#         perfil.save()

#         return redirect('login')

#     return render(request, 'users/signup.html')
