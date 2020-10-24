from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import AlertCoinSerializer      # add this
from .models import AlertCoin                     # add this

class AlertCoinView(viewsets.ModelViewSet):       # add this
  serializer_class = AlertCoinSerializer          # add this
  queryset = AlertCoin.objects.all()              # add this
