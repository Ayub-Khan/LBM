from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    date_created = models.DateField()


class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    contact = models.CharField(max_length=20)
    date_created = models.DateField()
    client_type = models.CharField(max_length=20)


class ImportExportEvents(models.Model):
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
    date_created = models.DateField()
