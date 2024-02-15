from django.contrib import admin

from carts.models import Cart


class CartTableAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']
    list_filter = ['created_timestamp', 'user', 'product']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Anonim'
    
    def product_display(self, obj):
        return str(obj.product.name)


