from rest_framework import serializers
from .models import FinanceData


# Serializer for display object attributes
class FinanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceData
        fields = '__all__'