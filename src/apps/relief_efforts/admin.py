from django.contrib import admin

from .models import ReliefEfforts

class ReliefEffortsAdmin(admin.ModelAdmin):
    list_display = ('id','relief_name', 'org_type', 'relief_type', 'status')
    search_fields = ('relief_name', 'org_type', 'relief_type', 'needs', 'status', 'severity_urgency')

admin.site.register(ReliefEfforts, ReliefEffortsAdmin)
