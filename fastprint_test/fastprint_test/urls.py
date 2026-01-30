"""
URL configuration for fastprint_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from produk.views_api import ProdukViewSet

router = DefaultRouter()
router.register(r'produk', ProdukViewSet)  # cukup 'produk', nanti URL jadi /api/produk/

def home_redirect(request):
    return redirect('produk_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect),                 # root diarahkan ke produk_list (HTML)
    path('produk/', include('produk.urls')), # HTML routes
    path('api/', include(router.urls)),      # API routes dengan prefix /api/
]
