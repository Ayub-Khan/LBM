from django import forms
from management.models import Company, Product


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
