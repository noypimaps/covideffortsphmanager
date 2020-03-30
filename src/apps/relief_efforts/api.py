from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, response
from .models import *
from .serializers import *


class OrganizationsViewset(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'


class ContactDetailsViewset(viewsets.ModelViewSet):
    queryset = ContactDetails.objects.all()
    serializer_class = ContactDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'


class BankDetailsViewset(viewsets.ModelViewSet):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'


class PricingDetailsViewset(viewsets.ModelViewSet):
    queryset = PricingDetails.objects.all()
    serializer_class = PricingDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'


class AddressDetailsViewset(viewsets.ModelViewSet):
    queryset = AddressDetails.objects.all()
    serializer_class = AddressDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'


class ItemizedNeedsViewset(viewsets.ModelViewSet):
    queryset = ItemizedNeeds.objects.all()
    serializer_class = ItemizedNeedsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'


class OtherDetailsViewset(viewsets.ModelViewSet):
    queryset = OtherDetails.objects.all()
    serializer_class = OtherDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = '__all__'
