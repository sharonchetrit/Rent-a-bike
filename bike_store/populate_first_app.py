import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from datetime import datetime
import random
from faker import Faker
from rent_app.models import Customer, Vehicle, Vehicle_type, Vehicle_size, Rental, Rental_rate

fakegen = Faker()

type_model_list = ['bike', 'scoot', 'trotinett']
size_list = ['small', 'medium', 'large']
cost = [120, 1500, 2000]

def add_size():
	for i in size_list:
		size = Vehicle_size.objects.get_or_create(name=random.choice(size_list))[0]
		size.save()
		return size 

def add_model():
	for i in type_model_list:
		model = Vehicle_type.objects.get_or_create(name=random.choice(type_model_list))[0]
		model.save()
		return model 


def populate_customer(N=10):
	for entry in range(N):

		fake_first_name = fakegen.first_name()
		fake_last_name = fakegen.last_name()
		fake_email = fakegen.email()
		fake_phone_number = fakegen.phone_number()
		fake_adress = fakegen.address()
		fake_city = fakegen.city()
		fake_country = fakegen.country()

		customer = Customer.objects.get_or_create(first_name=fake_first_name, 
												  last_name=fake_last_name, 
												  email=fake_email,
												  phone_number=fake_phone_number, 
												  address=fake_adress, 
												  city=fake_city, 
												  country=fake_country)[0]
	return customer


def populate_vehicle(N=20):
	model = add_model()
	size = add_size()

	for entry in range(N):

		fake_date_created = fakegen.date()
		fake_cost = fakegen.pyint()
		vehicle = Vehicle.objects.get_or_create(type_model=model, 
												date_created=fake_date_created, 
												real_cost=fake_cost, 
												size=size)[0]
	return vehicle

def populate_rental(N=10):
	for entry in range(N):

		fake_rental_date = fakegen.date_time_between(start_date="-1y", 
													 end_date="-7d", 
													 tzinfo=None)
		fake_return_date = fakegen.date_time_between_dates(datetime_start=fake_rental_date,
														   datetime_end=datetime.now(), 
														   tzinfo=None)

		rental = Rental.objects.get_or_create(rental_date=fake_rental_date, 
											  return_date=fake_return_date, 
											  customer=populate_customer(), 
											  vehicle=populate_vehicle())[0]


if __name__ == '__main__':
	print('Starting to populate...')
	# populate_customer(100)
	# populate_vehicle(20)
	populate_rental(10)
	print('Finish populating!')



