from django.contrib import admin
from django.urls import path , include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/' , include('core.urls')),
    path('verification/', include('verify_email.urls')),	
]
