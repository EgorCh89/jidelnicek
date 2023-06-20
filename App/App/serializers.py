from rest_framework import serializers
from home.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = [
            'title',
            'description'
        ]
