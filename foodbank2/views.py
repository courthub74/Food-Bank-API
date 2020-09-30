from django.shortcuts import render
from rest_framework import viewsets
from .models import FoodBank
from .serializers import FoodBankSerializer


class FoodBankView(viewsets.ModelViewSet):
	queryset = FoodBank.objects.all()
	serializer_class = FoodBankSerializer
