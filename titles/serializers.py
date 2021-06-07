from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

from .models import Category, Genre, Title, GenreTitle


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
        #extra_kwargs = {'url': {'lookup_field': 'slug'}}


class GenreTitleSerializer(serializers.ModelSerializer):
    
    genre = GenreSerializer(read_only=True)
    class Meta:
        model = GenreTitle
        fields = ('genre', 'title')
    

class TitleSerializer(serializers.ModelSerializer):

    category = CategotySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ('__all__')    

class TitleCreateSerializer(serializers.ModelSerializer):

    category = SlugRelatedField(many=False,
                                slug_field='slug',
                                queryset = Category.objects.all())
    genre = SlugRelatedField(many=True, slug_field='slug',
                                queryset = Genre.objects.all())

    class Meta:
        model = Title
        fields = ('__all__')  
    
    """
    def create(self, validated_data):
        genres = validated_data.pop('genre')
        category = validated_data.pop('category')
        title = self.Meta.model.objects.create(**validated_data)
        print(genres)
        for slug in genres:
            genre_obj, _ = Genre.objects.get_or_create(slug=slug)
            genre_title = GenreSerializer(data={'slug': slug})
            title.genres.add(genre_obj)

        title.save()
        return title  
    """
    

        
