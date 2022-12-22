from django import forms
from django.contrib import admin

from .models import students,modretur

admin .site.register(students)

admin .site.register(modretur)