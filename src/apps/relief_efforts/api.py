from rest_framework import viewsets
from .models import ReliefEfforts
from .serializers import ReliefEffortsSerializer

class ReliefEffortsViewset(viewsets.ModelViewSet):
    queryset = ReliefEfforts.objects.all()
    serializer_class = ReliefEffortsSerializer