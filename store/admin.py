from django.contrib import admin
from .models import Product

# Register your models here.


# class ProductAdmin(models.ModelAdmin):
#     list_display = ()


# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', "price", "category",
                    'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
