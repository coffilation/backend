import django_filters

from apps.compilations.models import Compilation


class CompilationsFilterSet(django_filters.FilterSet):
    compilationmembership__user__not = django_filters.NumberFilter(
        field_name='compilationmembership__user',
        exclude=True,
    )

    class Meta:
        model = Compilation
        fields = ['is_private', 'owner', 'places', 'compilationmembership__user']


class CompilationsPopulatedByPlaceInclusionFilterSet(django_filters.FilterSet):
    place = django_filters.NumberFilter(required=True, method='filter_by_place')

    def filter_by_place(self, queryset, name, value): # TODO сделать поле place обязательным нормальным способом
        return queryset

    class Meta:
        model = Compilation
        fields = ['is_private', 'owner', 'compilationmembership__user']
