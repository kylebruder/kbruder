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

    title = forms.CharField(max_length=256)
    slug = forms.SlugField(max_length=40)
    location = forms.CharField(
        max_length=256,
        required=False,
    )
    headline = forms.CharField(max_length=256)
    headline_img = CustomModelChoiceField(
        queryset = Image.objects.all(),
        required=False,
    )
    featured_img = CustomModelChoiceField(
        queryset = Image.objects.all(),
        required=False,
    )
    introduction = forms.CharField(
        max_length=5000,
        widget = Textarea,
        required=False,
    )
    content = forms.CharField(
        max_length=5000,
        widget = Textarea,
        required=False,
    )
    conclusion = forms.CharField(
        max_length=5000,
        widget = Textarea,
        required=False,
    )
    gallery = CustomModelChoiceField(
        queryset = Gallery.objects.all(),
        required=False,
    )
    artwork = CustomModelMultipleChoiceField(
        queryset = Piece.objects.all(),
        required=False,
    )
    artists = CustomModelMultipleChoiceField(
        queryset = Artist.objects.all(),
        required=False,
    )
    links = forms.ModelMultipleChoiceField(
        queryset = Link.objects.all(),
        required=False,
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

    def __init__(self, user, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['headline_img'].queryset = Image.objects.filter(user=user)
        self.fields['featured_img'].queryset = Image.objects.filter(user=user)
        self.fields['gallery'].queryset = Gallery.objects.filter(user=user)
        self.fields['artwork'].queryset = Piece.objects.filter(user=user)
        self.fields['artists'].queryset = Artist.objects.filter(user=user)
        self.fields['links'].queryset = Link.objects.filter(user=user)
