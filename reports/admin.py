from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
# Register your models here.
admin.site.register(Report, ReportAdmin)