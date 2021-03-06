from rest_framework import serializers
from .models import Size


class CartSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    variant = serializers.StringRelatedField()
    size = serializers.StringRelatedField()

    price = serializers.StringRelatedField()
    title = serializers.StringRelatedField()
    image = serializers.ImageField()
    properties = serializers.StringRelatedField()

    category = serializers.StringRelatedField()
    collection = serializers.StringRelatedField()

    class Meta:
        model = Size
        fields = '__all__'