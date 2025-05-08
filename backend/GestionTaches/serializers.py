from rest_framework import serializers
from .models import Taches

class tacheserializer(serializers.ModelSerializer):
    class Meta:
        model = Taches
        fields = '__all__'