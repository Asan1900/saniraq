"""
URL configuration for SaniraqProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_account.urls', namespace='account')),
    path('products/', include('app_product.urls', namespace='product')),
    path('stores/', include('app_store.urls', namespace='store')),
    path('carts/', include('app_cart.urls', namespace='cart')),
    path('orders/', include('app_order.urls', namespace='order')),
    path('likes/', include('app_like.urls', namespace='likes')),
    path('comments/', include('app_comment.urls', namespace='comments')),
]