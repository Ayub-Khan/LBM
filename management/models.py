from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Product(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True, editable=True)


class Company(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('management:list_companies')

    COMPANY_TYPES = (
        ('V', 'vendor'),
        ('C', 'client'),
    )
    company_type = models.CharField(max_length=1, choices=COMPANY_TYPES)

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    contact = models.IntegerField()
    date_created = models.DateField(auto_now_add=True, editable=True)


class ImportExportEvent(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    expense_description = models.CharField(max_length=200)
    total_stock_available = models.IntegerField()
    is_returned = models.BooleanField()
    expense = models.IntegerField()
    product_import = models.IntegerField()
    product_export = models.IntegerField()
    total_imported = models.IntegerField()
    cost = models.IntegerField()
    remaining_products = models.IntegerField()
    date_created = models.DateField(auto_now_add=True, editable=True)
