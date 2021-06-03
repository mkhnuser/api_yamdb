from rest_framework import serializers, validators

from .models import Category, Genre, Title


class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):

    category = CategotySerializer()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category')      

     
        
