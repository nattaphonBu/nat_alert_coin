from rest_framework import serializers
from .models import AlertCoin

class AlertCoinSerializer(serializers.ModelSerializer):
  class Meta:
    model = AlertCoin
    fields = ('id', 'title', 'description', 'completed')