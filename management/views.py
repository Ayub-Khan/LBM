from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView, View


class DashboardView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LBM'
        return context


dashboard_view = login_required(DashboardView.as_view())


class ClientProfileView(TemplateView):
    template_name = 'client_management/view_client_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LBM'
        return context


client_profile_view = login_required(ClientProfileView.as_view())


class ClientRegistrationView(View):
    template_name = 'client_management/create_client_profile.html'

    def get(self, request):
        return render(request, self.template_name)


client_registration_view = login_required(ClientRegistrationView.as_view())
