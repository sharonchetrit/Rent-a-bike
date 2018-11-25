from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

from rent_app.models import Customer, Rental, Vehicle, Vehicle_type, Vehicle_size, Rental_rate


def index(request):
	rentals = Rental.objects.all();
	print("qq", rentals);

	return render(request, 'index.html', {"data1": "test", "data2": "test2"})


def all_rentals(request):
	rentals = Rental.objects.all()

	return render(request, 'all_rentals.html', {'rentals': rentals})



def rental(request, rental_id):
	rental = Rental.objects.get(id=rental_id)

	return render(request, 'rental.html', {'rental': rental})


def add_rental_form(request):
	form = forms.AddRental()

	if request.method == 'POST':
		form = forms.AddRental(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('/rent_app/rental/')
		else:
			print('Error-Form is invalid')

	return render(request, 'add_rental_form.html', {'form': form})


def all_customers(request):
	customers = Customer.objects.order_by('first_name')

	return render(request, 'all_customers.html', {'customers': customers})


def customer(request, customer_id):
	customer = Customer.objects.get(id=customer_id)

	return render(request, 'customer.html', {'customer': customer})


def add_customer_form(request):
	form = forms.AddCustomer()

	if request.method == 'POST':
		form = forms.AddCustomer(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('/rent_app/customer/')

	return render(request, 'add_customer_form.html', {'form': form})
	