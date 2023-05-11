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
