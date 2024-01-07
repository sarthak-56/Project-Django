from django.contrib import admin

# Register your models here.
from .models import Customer
admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username','emailid',)

    