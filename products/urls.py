"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import products, basket_add, basket_remove

app_name = 'products'
# ctrl + D дублирует
urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'), #/products/baskets/app/<product_id>
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),  # /products/baskets/app/<product_id>
]
