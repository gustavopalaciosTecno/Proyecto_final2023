from django.urls import path
from . import views  # importamos las vistas de la app post


app_name = "post" # le damos un nombre a la app para evitar hardcodear en los templates


urlpatterns = [
    #path("", views.index, name="index"), 
    path('ver_post/<int:post_id>/', views.ver_post, name='ver_post'),
    path('post_list/', views.post_list, name="post_list"),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('editar_post/<int:id>/', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:id>/', views.eliminar_post, name='eliminar_post'),
    #path('realizar_comentario/<int:post_id>/', views.realizar_comentario, name='realizar_comentario'),
    #path('<int:post_id>/comentar/', views.realizar_comentario, name='realizar_comentario'),
    path('post/<int:post_id>/comentar/', views.realizar_comentario, name='realizar_comentario'),
    path('mostrar_categorias/', views.post_list, name='mostrar_categorias'),
    path('contact/', views.contact_form, name='contact_form'),
    path('buscar/', views.filtered_publications, name='buscar_posts'),


   
    ]

