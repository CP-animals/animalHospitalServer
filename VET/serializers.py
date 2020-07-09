from rest_framework import serializers
from VET.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'phone_number', 'address', 'name', 'location_x', 'location_y')