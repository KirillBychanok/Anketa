from django.contrib import admin
from .models import *


class WorkAdmin(admin.ModelAdmin):
    list_display = ('place', 'position', 'data_start', 'data_finish', 'tasks')
    ordering = ('place', 'data_start')


class AducationAdmin(admin.ModelAdmin):
    list_display = ('intitute', 'position', 'data_start', 'data_finish', 'progress')
    ordering = ('intitute', 'data_start')


admin.site.register(Soft)
admin.site.register(Hard)
admin.site.register(Work, WorkAdmin)
admin.site.register(Aducation, AducationAdmin)
