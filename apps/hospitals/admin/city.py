from django.contrib import admin
from apps.hospitals.models import City

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
         (None, {
            'fields': ['name'],
            'classes': ('wide', 'extrapretty'),
        }),
    ]
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']

admin.site.register(City, CityAdmin)
