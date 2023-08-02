from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from apps.user.forms import NewUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UpdateAvatarForm, RecuperarContrasenaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.contrib import messages
import random
import string


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = NewUserProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username') #claned_data sirve para obtener los datos del formulario
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                print('te logueaste')
                return redirect('index')
    context = {
        'form': form
    } 
    return render(request, 'auth/login.html', context)

def logoutUser(request):
    logout(request)
    print('te deslogueaste')
    return redirect('index')

def profile(request, id):
    user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(UserProfile, pk=id)
    form = UpdateAvatarForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            return redirect('user:profile', profile.id)
    context = {
        'user': user,
        'updateAvatarForm': form
    }
    return render(request, 'user/profile.html', context)
    

#controlar si funciona xd
# def changePassword(request):
#     user = request.user
#     form = PasswordChangeForm(data=request.POST or None, user=user)
#     if request.method == "POST":
#         if form.is_valid():
#             password = form.cleaned_data.get('new_password1')
#             user.set_password(password)
#             user.save()
#             return redirect('index')
#     context = {
#         'form': form
#     }
#     return render(request, 'auth/changePassword.html', context)

@login_required
def changePassword(request):
    user = request.user
    form = PasswordChangeForm(user=user)

    if request.method == "POST":
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:profile', id=user.id)

    context = {
        'form': form
    }
    return render(request, 'user/modificar_contrasena.html', context)

def recuperar_contrasena(request):
    form = RecuperarContrasenaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()

            if user:
                # Generar nueva contraseña aleatoria
                nueva_contrasena = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

                # Se requieren permisos y credenciales especiales
                #send_mail(
                #    'Recuperación de contraseña',
                #    f'Tu nueva contraseña es: {nueva_contrasena}',
                #    'tu_correo@ejemplo.com',  # Coloca tu dirección de correo electrónico aquí
                #    [email],
                #    fail_silently=False,
                #)

                # Actualizar la contraseña en la base de datos
                user.set_password(nueva_contrasena)
                user.save()

                messages.success(request, 'Se ha enviado un correo de recuperación de contraseña, bueno en realidad no, se requieren permisos especiales para correos de uso real.')
            else:
                messages.error(request, 'No se encontró una cuenta asociada al correo proporcionado.')

            return redirect('user:recuperar_contrasena')  # Redirigir de vuelta a la página de recuperación de contraseña

    context = {
        'form': form
    }

    return render(request, 'user/recuperar_contrasena.html', context)

def confirmar_recuperar_contrasena(request):
    return render(request,'user/confirmar_recuperar_contrasena.html')