from django.db import models
from django.utils.translation import gettext_lazy as _


class CompilationPermission(models.TextChoices):
    # Изменять данные коллекции
    CHANGE_COMPILATION = 'compilations.change_compilation', _('Изменение данных коллекции')

    # Изменять список точек в коллекции
    CHANGE_PLACES_LIST = 'compilation.change_places_list', _('Изменение списка точек в коллекции')
