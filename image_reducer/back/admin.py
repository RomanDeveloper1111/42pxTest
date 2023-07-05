from django.contrib import admin
from back.models import Reducer


@admin.register(Reducer)
class ReducerAdmin(admin.ModelAdmin):
    list_display = ['image', 'natural_image_name']

