from django.urls import include, path
from . import views

app_name = 'rent_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('rental/', views.all_rentals, name='all_rentals'),
	path('rental/<int:rental_id>/', views.rental, name='rental'),
	path('rental/add/', views.add_rental_form, name='add_rental_form'),
	path('customer/', views.all_customers, name="all_customers"),
	path('customer/<int:customer_id>/', views.customer, name='customer'),
	path('customer/add/', views.add_customer_form, name="add_customer_form"),
]