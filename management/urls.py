from django.urls import path
from django.conf.urls.static import static

from LBM import settings
from management import views

app_name = 'management'
urlpatterns = [
                  path('', views.dashboard_view, name='dashboard'),
                  path('view_client', views.client_profile_view, name='view_client'),
                  path('create_client', views.client_registration_view, name='create_client')
              ] + static(settings.STATIC_URL)
