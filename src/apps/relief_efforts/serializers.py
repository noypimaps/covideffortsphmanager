from rest_framework import serializers
from .models import ReliefEfforts

class ReliefEffortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliefEfforts
        fields = '__all__'
