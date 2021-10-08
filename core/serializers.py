from rest_framework import serializers

from .models import Client, Operation


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = '__all__'
