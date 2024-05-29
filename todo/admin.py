from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Todo

# Register your models here.
admin.site.register(Todo)
