from django.urls import path
from django.conf.urls.static import static

from LBM import settings
from management import views

app_name = 'management'
urlpatterns = [
                  path('', views.dashboard_view, name='dashboard'),
                  path('list_companies', views.companies_list_view, name='list_companies'),
                  path('create_company', views.company_registration_view, name='create_company'),
                  path('edit_company/<int:pk>/', views.company_edit_view, name='edit_company'),
                  path('view_company/<int:pk>/', views.company_profile_view, name='view_company'),
                  path('delete_company/<int:pk>/', views.company_delete_view, name='delete_company'),
                  path('list_products', views.products_list_view, name='list_products'),
                  path('create_product', views.product_registration_view, name='create_product'),
                  path('edit_product/<int:pk>/', views.product_edit_view, name='edit_product'),
                  path('view_product/<int:pk>/', views.product_profile_view, name='view_product'),
                  path('delete_product/<int:pk>/', views.product_delete_view, name='delete_product'),
              ] + static(settings.STATIC_URL)
