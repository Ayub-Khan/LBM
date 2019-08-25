from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from LBM import settings

app_name = 'management'
urlpatterns = [

    path(
        '',
        login_required(TemplateView.as_view(template_name='home_page.html')),
        name='dashboard'
    ),

] + static(settings.STATIC_URL)
