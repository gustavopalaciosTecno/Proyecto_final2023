from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria, User, Comentario
from .forms import ComentarioForm, PostForm
from django import forms
#from apps.post.forms import publicacionForm ##donde esta publicacionForm??? D:
from django.forms import modelform_factory
from django.core.paginator import Paginator
from datetime import date
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    # Obtener los últimos posteos
    posts = Post.objects.order_by('-fecha_publicacion')[:5]
    
    return render(request, 'post/index.html', {'posts': posts})

    
def categorias(request):
    return render(request, 'categorias.html')


def ver_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentario_set.all()#trae todos los comentarios de este post en particular
    context = {
        'publicacion': post,
        'comentarios': comentarios,
    }
    return render(request, 'post/post_detail.html', context) #crear html de post

#USAR PAGINADO CON PAGINATOR
   
def post_list(request):
  
    posts = Post.objects.all()
    comentarios = Comentario.objects.all()
    
   
    context = {
        'post': posts,
        'comentarios': comentarios,
        
    }

    return render(request, 'post/post_list.html', context)

def post_list2(request):
    categorias = Categoria.objects.all()
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')

    if query:
        posts = Post.objects.filter(titulo__icontains=query)
    elif categoria_id:
        posts = Post.objects.filter(categoria_id=categoria_id)
    else:
        posts = Post.objects.all()

    context = {
        'posts': posts,
        'categorias': categorias,
    }
    return render(request, 'post/post_list.html', context)

# @login_required
# def crear_post(request):
#     publicacionForm = modelform_factory(Post, exclude=['fecha_actualizacion'])
#     if request.method == 'POST':
#         formPost = publicacionForm(request.POST)
#         if formPost.is_valid():
#             post = formPost.save(commit=False)  # Guardamos el formulario sin guardar en la base de datos aún.
#             post.autor = request.user  # Asignamos el autor al usuario actualmente autenticado.
#             post.save()  # Ahora guardamos la publicación en la base de datos.
#             #print(post.id)
#             #return redirect('ver_post', post.id)  # Redirigir a la página de ver_post.
#     else:
#         formPost = publicacionForm()   
#     return render(request, 'post/new_post.html', {'formPost': formPost})

# @login_required
# def crear_post(request):
#     if request.method == 'POST':
#         formPost = PostForm(request.POST)
#         if formPost.is_valid():
#             post = formPost.save(commit=False)
#             post.autor = request.user
#             post.save()
#             return redirect('ver_post', post_id = post.id)
#     else:
#         formPost = PostForm()
#     return render(request, 'post/new_post.html', {'formPost': formPost})

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['fecha_actualizacion']
@login_required
def crear_post(request):
    if request.method == 'POST':
        formPost = PostForm(request.POST)
        if formPost.is_valid():
            post = formPost.save(commit=False)
            post.autor = request.user
            post.save()
            #return redirect('post_list')
            return redirect('post:ver_post', post_id=post.id)
             # Use the name of the URL pattern and pass the 'post_id'
    else:
        formPost = PostForm()
    return render(request, 'post/new_post.html', {'formPost': formPost})

@login_required
def editar_post(request, id):
    publicacion = get_object_or_404(Post, pk=id)
    publicacionForm = modelform_factory(Post, exclude=['fecha_actualizacion'])
    
    if request.method == 'POST':
        formPost = publicacionForm(request.POST, instance=publicacion)
        if formPost.is_valid():
            formPost.save()
            return redirect('post:post_list')  # Usamos post_id en lugar de id
    else:
        formPost = publicacionForm(instance=publicacion)
        
    return render(request, 'post/update_post.html', {'formPost': formPost})


@login_required
def eliminar_post(request, id):
    publicacion = get_object_or_404(Post, pk=id)
    if (request.user == publicacion.autor ):
        if request.method == 'POST':
            publicacion.delete()
            return redirect('post:post_list')
    else:
        return redirect('index')     
    return render(request, 'post/delete_post.html',{'publicacion':publicacion})

 


def realizar_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(post=post)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('post:post_list')
           
    else:
        form = ComentarioForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/realizar_comentario.html', context)

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

       
        send_mail(
            'Formulario de contacto - ' + name,
            'Email: ' + email + '\nMensaje: ' + message,
            'project_manageer@protonmail.com',  
            ['project_manageer@protonmail.com'],  
            fail_silently=False,
        )

  
        return HttpResponseRedirect(reverse('contact_form', kwargs={'message_sent': True}))
    
 
    return render(request, 'contact.html', {'message_sent': False})



def filtered_publications(request):
    filter_term = request.GET.get('filter', '')  
    filtered_publications = Post.objects.filter(titulo__icontains=filter_term)

    context = {
        'publicaciones': filtered_publications,
        'titulo': f'Publicaciones con título que contiene "{filter_term}"',
        
    }

    return render(request, 'buscar_posts.html', context)









