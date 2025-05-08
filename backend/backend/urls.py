
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GestionTaches.urls')),  # Assurez-vous d'inclure les URLs de votre application

]
