from django.contrib import admin
from .models import Objective, Priority, Status, GitBranch

# Register your models here.

admin.site.register(Objective)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(GitBranch)
