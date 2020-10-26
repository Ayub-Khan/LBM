from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    UpdateView, ListView,
    CreateView, DeleteView
)

from management.forms import CompanyForm
from management.models import Company


class CompanyProfileView(DetailView):
    model = Company
    template_name = 'company_management/view_company_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LBM-Company List'
        return context


company_profile_view = login_required(CompanyProfileView.as_view())


class CompaniesListView(ListView):
    model = Company
    template_name = 'company_management/list_companies.html'
    context_object_name = 'companies'


companies_list_view = login_required(CompaniesListView.as_view())


class CompanyRegistrationView(CreateView):
    model = Company
    form_class = CompanyForm
    context_object_name = 'company'
    template_name = 'company_management/create_company_profile.html'


company_registration_view = login_required(CompanyRegistrationView.as_view())


class CompanyEditView(UpdateView):
    model = Company
    form_class = CompanyForm
    context_object_name = 'company'
    template_name = 'company_management/edit_company_profile.html'


company_edit_view = login_required(CompanyEditView.as_view())


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_management/confirm_delete.html'
    success_url = reverse_lazy('management:list_companies')


company_delete_view = login_required(CompanyDeleteView.as_view())
