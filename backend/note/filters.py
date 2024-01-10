from django.utils.text import slugify
from django_filters import rest_framework as filters

from note.models import Note
from django.db.models import Q


class NoteFilter(filters.FilterSet):
    is_trash = filters.BooleanFilter(field_name='is_trash')
    word = filters.CharFilter(method='filter_word')

    def filter_word(self, queryset, name, value):
        filter_value = slugify(value)
        return queryset.filter(Q(slug__icontains=filter_value) | Q(body__icontains=filter_value))

    class Meta:
        model = Note
        fields = ["is_trash", "word"]
