from django_filters import rest_framework as filters

from .models import Title


class TitleFilter(filters.FilterSet):
    genre = filters.filters.CharFilter(
        field_name="genre__slug", method='filter_genre')
    category = filters.filters.CharFilter(
        field_name="category__slug", method='filter_category')
    name = filters.filters.CharFilter(
        field_name="name", lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']

    def filter_genre(self, queryset, name, value):
        return queryset.filter(genre__slug__icontains=value)

    def filter_category(self, queryset, name, value):
        return queryset.filter(category__slug__icontains=value)
