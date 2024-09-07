from rest_framework import serializers
from .models import Walet

class WaletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walet
        fields = '__all__'


class UpateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walet
        fields = ['wallet',]