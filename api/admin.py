from django.contrib import admin
from .models import Customer, Product, Sale


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('get_customer', 'get_product', 'date', 'time', 'amount')

    def get_customer(self, obj):
        return obj.customer.name

    def get_product(self, obj):
        return obj.product.name


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
