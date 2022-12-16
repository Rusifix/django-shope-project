from django.contrib import admin
from products.models import ProductCategory, Product, Basket

# Register your models here.
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantite')
    fields = ('name', 'description', 'image', 'category', 'quantite')
    ordering = ('name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantite')