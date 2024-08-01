# Generated by Django 5.0.7 on 2024-07-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.IntegerField()),
                ('CustomerName', models.CharField(max_length=30)),
                ('Product', models.CharField(max_length=50)),
                ('ProductPrice', models.IntegerField()),
                ('CustomerPhone', models.BigIntegerField()),
                ('CustomerEmail', models.EmailField(max_length=254)),
                ('CustomerAddress', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=50)),
            ],
        ),
    ]