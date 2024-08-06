from rest_framework import serializers

from .models import OrderModel



class getserilaze(serializers.ModelSerializer):
    class Meta:
        model=OrderModel
        fields="__all__"
