from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView , LogoutView 

urlpatterns = [
    path("login/" , views.Login.as_view() , name ="login") , 
    path('register/' , views.Register.as_view() , name='register'),
    path('logout/' , LogoutView.as_view(next_page='login'),name='loout'),

    path('' , views.Home.as_view() , name='home') , 
    path('delete/<int:pk>/' , views.DeleteTask.as_view() , name='delete')
]
 