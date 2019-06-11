from django.conf.urls import url
from django.conf.urls.static import static

from management import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
