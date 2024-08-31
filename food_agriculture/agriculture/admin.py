from django.contrib import admin
from .models import Crop, Farmer, Investment

# Register your models here.
admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(Investment)