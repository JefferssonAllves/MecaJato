from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),
    
    
]
