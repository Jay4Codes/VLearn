from rest_framework import serializers

from .models import *

class csvserializer(serializers.ModelSerializer):
    class Meta:
        model = csvstorage
        fields = '__all__'