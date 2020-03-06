from django.contrib import admin
from .models import Tag, Link, FeaturedImage, HeadlineImage, Image, Gallery, Update
# Register your models here.

admin.site.register(Tag)
admin.site.register(Link)
admin.site.register(FeaturedImage)
admin.site.register(HeadlineImage)
admin.site.register(Image)
admin.site.register(Gallery)
admin.site.register(Update)
