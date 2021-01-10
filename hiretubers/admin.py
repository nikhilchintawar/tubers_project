from django.contrib import admin
from .models import Hiretuber

# Register your models here.
@admin.register(Hiretuber)
class HiretuberAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'email', 'city')
    list_display_links=('first_name',)
    search_fields=('first_name', 'city')
    ordering=['id']

# admin.site.register(Hiretuber)