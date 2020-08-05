from django.contrib import admin

# Register your models here.
from . import Okaty
from .models import UserProfile
admin.site.register(UserProfile)
