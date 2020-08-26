from django.contrib import admin

from .models import Company, Product, ImportExportEvent

# Register your models here.
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ImportExportEvent)
