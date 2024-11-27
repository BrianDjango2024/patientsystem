from django.contrib import admin
from .models import Specialist, Record

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialist')
    list_display_links = ('id', 'specialist')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'condition')
    list_display_links = ('id', 'patient_name', 'condition')

admin.site.register(Specialist, SpecialistAdmin)

admin.site.register(Record, RecordAdmin)