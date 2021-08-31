from django.contrib import admin
# adding your library and model
from .models import Snacks

# Register your models here.
admin.site.register(Snacks)
