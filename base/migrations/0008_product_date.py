# Generated by Django 3.2.9 on 2022-06-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20220606_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Добавить дату'),
        ),
    ]