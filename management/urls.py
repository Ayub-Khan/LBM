from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static

from LBM import settings

app_name = 'management'
urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
] + static(settings.STATIC_URL)
