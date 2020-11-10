from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView
)


class DashboardView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'LBM-Dashboard'
        return context


dashboard_view = login_required(DashboardView.as_view())
