"""
URL configuration for derssec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import ogretmen.views
import ogrenci.views
import anasayfa.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("ogretmen/",ogretmen.views.ogretmenanasayfa),
    path("ogrenci/",ogrenci.views.ogrencianasayfa, name="ogrenciler"),
    path("anasayfa/",anasayfa.views.anatr),
    path("",anasayfa.views.anatr),
    path("ogrenci/liste",ogrenci.views.ogrencilistesi),
    path("ogrenci/ekle",ogrenci.views.ekle),
    path('ogrenciler/detay/<int:id>', views.detay, name='detay'),





]
