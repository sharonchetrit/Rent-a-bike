from django.db import models

# Create your models here.

class Customer(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	email = models.EmailField()
	phone_number = models.CharField(max_length=20)
	address = models.CharField(max_length=264)
	city = models.CharField(max_length=264)
	country = models.CharField(max_length=264)

	def __repr__(self):
		return "<User {} {}>".format(self.first_name, self.last_name)

	def __str__(self):
		return '%s, %s' %(self.first_name, self.last_name)

class Vehicle_type(models.Model):
	name = models.CharField(max_length=264)

	def __repr__(self):
		return "<Vehicle {}>".format(self.name)

	def __str__(self):
		return self.name



class Vehicle_size(models.Model):
	name = models.CharField(max_length=264)


class Vehicle(models.Model):
	type_model = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
	date_created = models.CharField(max_length=264)
	real_cost = models.CharField(max_length=264)
	size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)

	def __repr__(self):
		return "<Vehicle {}>".format(self.type_model.name)

	def __str__(self):
		return self.type_model.name


class Rental(models.Model):
	rental_date = models.DateField(max_length=264)
	return_date = models.DateField(max_length=264)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

	def __repr__(self):
		return "<Returned on: {}>".format(self.return_date)

	def __str__(self):
		return self.return_date


class Rental_rate(models.Model):
	daily_rate = models.CharField(max_length=264)
	vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
	vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)