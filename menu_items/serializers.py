from rest_framework import serializers
from .models import Item

class NewItemSerializer(serializers.Serializer):
    Location = serializers.DictField(
        child=serializers.CharField(),
        required=True
    )
    Persona = serializers.DictField(
        child=serializers.CharField(),
        required=True
    )
    Audio = serializers.URLField(required=True)
    Image = serializers.URLField(required=True)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'