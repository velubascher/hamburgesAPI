# Generated by Django 3.0.5 on 2020-04-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='api.Ingrediente'),
        ),
    ]
