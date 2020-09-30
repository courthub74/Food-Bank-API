from rest_framework import serializers
from .models import FoodBank

class FoodBankSerializer(serializers.ModelSerializer):
	class Meta:
		model = FoodBank
		fields = ('id', 'name', 'address', 'city', 'state', 'zipcode', 'phone', 'details', 'weblink', 'photo')