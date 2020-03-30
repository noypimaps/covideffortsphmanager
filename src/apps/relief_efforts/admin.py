from django.contrib import admin

from .models import *

class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ('id','org_name', 'org_type', 'severity_urgency', 'status')
    search_fields = ('org_name', 'org_type', 'status', 'severity_urgency')

class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','org', 'name', 'contact_number')
    search_fields = ('org', 'name', 'contact_number')

class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','contact_details', 'bank_name', 'account_number', 'account_number')
    search_fields = ('contact_details', 'bank_name', 'account_number', 'account_number')

class PricingDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','org', 'name_of_item', 'unit', 'unit_price')
    search_fields = ('org', 'name_of_item', 'unit', 'unit_price')

class AddressDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','org', 'city_municipality', 'province', 'region')
    search_fields = ('org', 'city_municipality', 'province', 'region')

class OtherDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','org', 'link_for_more_info', 'link_to_poster')
    search_fields = ('org', 'who_they_help', 'what_they_do')

class ItemizedNeedsAdmin(admin.ModelAdmin):
    list_display = ('id','org', 'name_of_item', 'unit', 'received_inventories', 'total_need')
    search_fields = ('org', 'name_of_item', 'unit', 'received_inventories', 'total_need')


admin.site.register(ItemizedNeeds, ItemizedNeedsAdmin)
admin.site.register(OtherDetails, OtherDetailsAdmin)
admin.site.register(AddressDetails, AddressDetailsAdmin)
admin.site.register(PricingDetails, PricingDetailsAdmin)
admin.site.register(BankDetails, BankDetailsAdmin)
admin.site.register(ContactDetails, ContactDetailsAdmin)
admin.site.register(Organizations, OrganizationsAdmin)
