from django.urls import path
from django.conf.urls.static import static

from LBM import settings
from management import views

app_name = 'management'
urlpatterns = [
                  path('', views.dashboard, name='dashboard')
              ] + static(settings.STATIC_URL)
