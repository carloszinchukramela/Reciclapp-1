from django.contrib import admin
from .models import Oferente
from .models import Desecho
from .models import TipoDesecho

admin.site.register(Oferente)
admin.site.register(Desecho)
admin.site.register(TipoDesecho)
