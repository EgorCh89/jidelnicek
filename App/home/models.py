from django.db import models


class Meal(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    ingredients = models.CharField(max_length=500)
    guideline = models.CharField(max_length=1000)
    public = models.BooleanField(default=False)
    type = models.CharField(
        choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')], max_length=20)


class DayPlan(models.Model):

    breakfast = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='breakfast')
    lunch = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='lunch')
    dinner = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='dinner')
