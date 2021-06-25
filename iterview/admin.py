from django.contrib import admin
from .models import Entrevistado, Entrevistador, Empresa, Agendar, Reunion

#Objetos de la BBDD (definidos en models.py)

admin.site.register(Entrevistado)
admin.site.register(Entrevistador)
admin.site.register(Empresa)
admin.site.register(Agendar)
admin.site.register(Reunion)