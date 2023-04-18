from django.contrib.auth.models import User
from django.db import models
from apps.compilations.models import Compilation


class CompilationMembership(models.Model):
    compilation = models.ForeignKey(Compilation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.compilation}, {self.user}'
