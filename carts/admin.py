from django.contrib import admin

from carts.models import Cart, CartItem

# Register your models here.


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "cart", "quantity", "is_active")


@admin.register(Cart)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart_id", "date_added")
