from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=200, help_text='Name of model')
    slug = models.SlugField(verbose_name='url', unique=True,
                            help_text='slug of group', null=True)

    class Meta:
        verbose_name = 'Genre'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=200, help_text='Name of category')
    slug = models.SlugField(verbose_name='url', unique=True,
                            help_text='slug of category', null=True)

    class Meta:
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(verbose_name='name',
                            max_length=200, help_text='Title')
    year = models.IntegerField(verbose_name='year', help_text='Year of title')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField('Genre', through='GenreTitle')
    description = models.TextField(verbose_name='description', null=True)

    class Meta:
        verbose_name = 'Title'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['genre', 'title'], name='composite_key')
        ]


class Review(models.Model):
    title = models.ForeignKey(
        'titles.Title',
        verbose_name='Объект обзора',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField('Текст')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Обзор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField('Текст')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
