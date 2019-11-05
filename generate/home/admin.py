from django.contrib import admin
from .models import (
                        OptionGenerate,
                        Directory,
                        Departament
                    )
# Register your models here.

admin.site.register(OptionGenerate)
admin.site.register(Directory)
admin.site.register(Departament)
