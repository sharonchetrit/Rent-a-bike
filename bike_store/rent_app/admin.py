from django.contrib import admin
from rent_app.models import Customer, Rental, Vehicle

# Register your models here.
admin.site.register(Customer)
admin.site.register(Rental)
admin.site.register(Vehicle)