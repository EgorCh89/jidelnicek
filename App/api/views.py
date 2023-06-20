from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from App.serializers import *
# Create your views here.


@api_view(['GET'])
def api_home(request, *args, **kwargs):

    instance = Meal.objects.all()
    data = {}
    if instance:
        data = MealSerializer(instance).data
    return Response(data)
