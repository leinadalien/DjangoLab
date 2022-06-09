from django.contrib import admin

from .models import *


class ScamerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'money', 'time_create')
    search_fields = ('name',)


admin.site.register(Scamer, ScamerAdmin)
