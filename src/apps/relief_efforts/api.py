from rest_framework import viewsets
from .models import *
from .serializers import *


class OrganizationsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializer

class ContactDetailsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ContactDetails.objects.all()
    serializer_class = ContactDetailsSerializer

class BankDetailsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializer

class PricingDetailsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = PricingDetails.objects.all()
    serializer_class = PricingDetailsSerializer

class AddressDetailsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = AddressDetails.objects.all()
    serializer_class = AddressDetailsSerializer

class ItemizedNeedsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ItemizedNeeds.objects.all()
    serializer_class = ItemizedNeedsSerializer

class OtherDetailsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = OtherDetails.objects.all()
    serializer_class = OtherDetailsSerializer