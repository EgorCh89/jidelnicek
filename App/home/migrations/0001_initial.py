# Generated by Django 4.2.1 on 2023-06-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('ingredients', models.CharField(max_length=500)),
                ('guideline', models.CharField(max_length=1000)),
                ('public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DayPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breakfast', to='home.meal')),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinner', to='home.meal')),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lunch', to='home.meal')),
            ],
        ),
    ]