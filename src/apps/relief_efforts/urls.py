from rest_framework import routers
from .api import ReliefEffortsViewset

router = routers.DefaultRouter()
router.register(r'relief-efforts', ReliefEffortsViewset)
