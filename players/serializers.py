from rest_framework import serializers
from .models import Player  # Assuming your Player model is in the same app

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'  # Include all fields of the Player model
