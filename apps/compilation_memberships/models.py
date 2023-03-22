from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from apps.compilations.models import Compilation


class CompilationMembershipRole(models.IntegerChoices):
    MEMBER = 0, _('Member')  # Без прав
    EDITOR = 1, _('Editor')  # Может добавлять точки в коллекцию и менять её данные
    ADMIN = 2, _('Admin')  # Может повышать до editor'a и удалять участников
    OWNER = 3, _('Owner')  # Может всё


class CompilationMembership(models.Model):
    compilation = models.ForeignKey(Compilation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.IntegerField(
        choices=CompilationMembershipRole.choices,
        default=CompilationMembershipRole.MEMBER
    )

    def __str__(self):
        return f'{self.compilation}, {self.user}, {self.get_role_display()}'

    class Meta:
        constraints = [UniqueConstraint(
            fields=['compilation', 'user'],
            name='compilation_membership_unique_constraint'
        )]
