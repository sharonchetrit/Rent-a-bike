from django import forms
from rent_app.models import Rental, Customer

#my classes

class AddRental(forms.ModelForm):
	class Meta():
		model = Rental
		fields = '__all__'

class AddCustomer(forms.ModelForm):
	class Meta():
		model = Customer
		fields = '__all__'