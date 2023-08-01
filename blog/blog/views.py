from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.contrib.auth.models import User
from apps.post.models import Post


def index(request):
    post_recientes = Post.objects.all().order_by('-fecha_creacion')[0:4]
    context = {
        'post_recientes':post_recientes
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contacto(request):
    contacto = "3731-498413"
    return render(request, "contact.html",{
        "contacto":contacto,
    })

def about(request):
    usuarios = User.objects.all()
    correos = User.objects.all()
    return render(request, "about.html",{
        "usuarios":usuarios,
        "correos":correos,
    })
    

  