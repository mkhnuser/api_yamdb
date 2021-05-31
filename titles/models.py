from django.db import models


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
    genres = models.ManyToManyField('Genre', through='GenreTitle')

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
