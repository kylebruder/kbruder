from django.contrib import admin
from people.models import Person, Artist, Quote

# Register your models here.
admin.site.register(Person)
admin.site.register(Artist)
admin.site.register(Quote)
