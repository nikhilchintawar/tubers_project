from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def my_photo(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ('id', 'my_photo','first_name', 'role', 'created_date')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def my_photo(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    list_display = ('id', 'my_photo','headline', 'link', 'created_date')
    list_display_links = ('headline',)
    search_fields = ('headline',)
    list_filter = ('headline',)

# admin.site.register(Slider, SliderAdmin)
# admin.site.register(Team, TeamAdmin)