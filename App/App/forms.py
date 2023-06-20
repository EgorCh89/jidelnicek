from django import forms
from home.models import Meal


class MealForm(forms.Form):
    class Meta:
        model = Meal
        fields = [
            'title',
            'description'
        ]
