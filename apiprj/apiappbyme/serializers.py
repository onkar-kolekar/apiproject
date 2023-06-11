from rest_framework import serializers
from .models import apiModel

class serializeClass(serializers.ModelSerializer):
    class Meta:
        model=apiModel
        fields='__all__'
