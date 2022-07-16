"""
Serializer fro recipe api
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""

    class Meta:
        model = Recipe
        fields = ['id','title','time_minuite', 'price','link']
        read_only_fields = ['id']