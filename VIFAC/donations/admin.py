from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Donor, Donation, Category)
class DonorAdmin(admin.ModelAdmin): pass
class DonationAdmin(admin.ModelAdmin): pass
class CategoryAdmin(admin.ModelAdmin): pass

