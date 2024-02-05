from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    empty_value_display = '-отсутствует-'
    list_display = ('name', 'parent', 'url')
    list_editable = ('url',)
    list_filter = ('parent',)
    list_display_links = ('parent',)
    read_only_field = ('url',)
    searh_field = ('name', 'parent')
    save_on_top = True
