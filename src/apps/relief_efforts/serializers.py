from rest_framework import serializers
from .models import *

class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'


class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = '__all__'

class OtherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDetails
        fields = '__all__'

class PricingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingDetails
        fields = '__all__'

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'


class ItemizedNeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemizedNeeds
        fields = '__all__'
