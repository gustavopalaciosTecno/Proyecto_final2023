from django.urls import path
from . import views  

app_name = "user" 
urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("changePassword/", views.changePassword, name="changePassword"),
    path('modificar_contrasena/', views.changePassword, name='modificar_contrasena'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('confirmar_recuperar_contrasena/', views.confirmar_recuperar_contrasena, name='confirmar_recuperar_contrasena'),
    ]  