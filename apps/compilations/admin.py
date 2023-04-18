from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Compilation


class CompilationAdmin(GuardedModelAdmin):
    pass


admin.site.register(Compilation, CompilationAdmin)
