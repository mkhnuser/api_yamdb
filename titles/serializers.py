from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .models import Category, Genre, GenreTitle, Title, Review, Comment
from django.db.models import Avg


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


class GenreTitleSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(read_only=True)

    class Meta:
        model = GenreTitle
        fields = ('genre', 'title')


class TitleSerializer(serializers.ModelSerializer):

    category = CategotySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField(method_name='calculate_rating')

    class Meta:
        model = Title
        fields = ('__all__')

    def calculate_rating(self, instance):
        avg_score = instance.reviews.aggregate(score_avg=Avg('score')).get('score_avg')
        if avg_score is None:
            return None
        return int(avg_score)


class TitleCreateSerializer(serializers.ModelSerializer):

    category = SlugRelatedField(many=False,
                                slug_field='slug',
                                queryset=Category.objects.all())
    genre = SlugRelatedField(many=True, slug_field='slug',
                             queryset=Genre.objects.all())

    class Meta:
        model = Title
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, attrs):
        attrs['title'] = get_object_or_404(
            Title, id=self.context['view'].kwargs['title_id'])
        if not self.partial and Review.objects.filter(
                title=attrs['title'],
                author=self.context['request'].user).exists():
            raise ValidationError(
                {'author': 'Вы уже оставляли отзыв на это произведение'})
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')

    def validate(self, attrs):
        attrs['review'] = get_object_or_404(
            Review,
            id=self.context['view'].kwargs['review_id'],
            title_id=self.context['view'].kwargs['title_id']
        )
        return attrs
