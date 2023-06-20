from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ("cnpj", "razaosocial",)

# Register your models here.
admin.site.register(Vendor, VendorAdmin)