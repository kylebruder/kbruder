from django import forms
from django.forms.widgets import Textarea, RadioSelect, CheckboxInput
from .models import Update
from images.models import Image, Gallery, Piece
from links.models import Link
from people.models import Artist
from templates.widgets import ImagePreviewWidget

class CustomModelChoiceIterator(forms.models.ModelChoiceIterator):

    def choice(self, obj):
        return self.field.prepare_value(obj), self.field.label_from_instance(obj), obj

class CustomModelChoiceField(forms.models.ModelChoiceField):

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return CustomModelChoiceIterator(self)

    choices = property(_get_choices, forms.ChoiceField._set_choices)

class CustomModelMultipleChoiceField(forms.models.ModelMultipleChoiceField):

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return CustomModelChoiceIterator(self)

    choices = property(_get_choices, forms.MultipleChoiceField._set_choices)

class UpdateForm(forms.ModelForm):

    headline_img = CustomModelChoiceField(
        queryset=Image.objects.all(),
        required=False,
        help_text=Update._meta.get_field('headline_img').help_text,
    )
    featured_img = CustomModelChoiceField(
        queryset=Image.objects.all(),
        required=False,
        help_text=Update._meta.get_field('featured_img').help_text,
    )
    gallery = CustomModelChoiceField(
        queryset=Gallery.objects.all(),
        required=False,
        help_text=Update._meta.get_field('gallery').help_text,
    )
    artwork = CustomModelMultipleChoiceField(
        queryset=Piece.objects.all(),
        required=False,
        help_text=Update._meta.get_field('artwork').help_text,
    )
    artists = CustomModelMultipleChoiceField(
        queryset=Artist.objects.all(),
        required=False,
        help_text=Update._meta.get_field('artists').help_text,
    )
    
    class Meta:
        model = Update
        
        fields = (
            'title',
            'slug',
            'location',
            'headline',
            'headline_img',
            'featured_img',
            'introduction',
            'content',
            'conclusion',
            'gallery',
            'artwork',
            'artists',
            'links',
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['headline_img'].queryset = Image.objects.filter(
            user=user,
        ).order_by(
            '-creation_date',
        )
        self.fields['featured_img'].queryset = Image.objects.filter(
            user=user,
        ).order_by(
            '-creation_date',
        )
        self.fields['gallery'].queryset = Gallery.objects.filter(
            user=user,
        ).filter(
            is_public=True,
        ).order_by(
            '-publication_date',
        )
        self.fields['artwork'].queryset = Piece.objects.filter(
            user=user,
        ).filter(
            is_public=True,
        ).order_by(
            '-publication_date',
        )
        self.fields['artists'].queryset = Artist.objects.filter(
            user=user,
        ).filter(
            is_public=True,
        ).order_by(
            '-publication_date',
        )
        self.fields['links'].queryset = Link.objects.filter(
            user=user,
        ).order_by(
            '-publication_date',
        )
