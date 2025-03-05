from rest_framework import serializers
from .models import CRUD_model


class CRUD_serializer(serializers.ModelSerializer):
    class Meta:
        model = CRUD_model
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']
