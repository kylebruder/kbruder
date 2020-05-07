from django.contrib import admin
from .models import Unit, Currency, Degree, Distance, Mass, Volume

# Register your models here.
admin.site.register(Unit)
admin.site.register(Currency)
admin.site.register(Degree)
admin.site.register(Distance)
admin.site.register(Mass)
admin.site.register(Volume)
