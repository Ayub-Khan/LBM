from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    UpdateView, ListView,
    CreateView, DeleteView
)

from management.forms import ProductForm
from management.models import Product


class ProductProfileView(DetailView):
    model = Product
    template_name = 'product_management/view_product_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LBM'
        return context


product_profile_view = login_required(ProductProfileView.as_view())


class ProductsListView(ListView):
    model = Product
    template_name = 'product_management/list_products.html'
    context_object_name = 'products'


products_list_view = login_required(ProductsListView.as_view())


class ProductRegistrationView(CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product_management/create_product_profile.html'


product_registration_view = login_required(ProductRegistrationView.as_view())


class ProductEditView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product_management/edit_product_profile.html'


product_edit_view = login_required(ProductEditView.as_view())


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'company_management/confirm_delete.html'
    success_url = reverse_lazy('management:list_products')


product_delete_view = login_required(ProductDeleteView.as_view())
