from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import TemplateView
from images.models import Image, Gallery
from links.models import Link
from updates.models import Update

# Create your views here.

class StudioView(TemplateView):

    template_name = 'studio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=context['user'])
        context['galleries'] = Gallery.objects.filter(
            user=user).order_by(
                'is_public', 
                '-creation_date',
        )[:10]
        #context['images'] = 
        context['links'] = Link.objects.filter(
            user=user).order_by(
                '-creation_date',
        )[:10]
        context['updates'] = Update.objects.filter(
            user=user).order_by(
                'is_public',
                '-creation_date',
        )[:10]
        return context
