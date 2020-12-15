from rest_framework import serializers
from . models import PlaceDetails

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceDetails
        fields = '__all__'