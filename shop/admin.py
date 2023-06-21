from django.contrib import admin
from shop.models import Product, Category

class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Categoryadmin)

class Productadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','category','available','updated']
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Product,Productadmin)



