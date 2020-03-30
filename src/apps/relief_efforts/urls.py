from django.urls import path, include
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationsViewset)
router.register(r'bank-details', BankDetailsViewset)
router.register(r'other-details', OtherDetailsViewset)
router.register(r'contact-details', ContactDetailsViewset)
router.register(r'address-details', AddressDetailsViewset)
router.register(r'pricing-details', PricingDetailsViewset)
router.register(r'itemized-needs', ItemizedNeedsViewset)

urlpatterns = [
    path('', include(router.urls)),
]