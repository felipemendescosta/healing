from django.contrib import admin
from .models import Especialidades, DadosMedicos, DatasAbertas
from .models import DadosMedicos

admin.site.register(Especialidades)
admin.site.register(DadosMedicos)
admin.site.register(DatasAbertas)

# Register your models here.
