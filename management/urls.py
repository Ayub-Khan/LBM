from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static

from management import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'signup/', views.SignUP, name='signup'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
