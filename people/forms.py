from django import forms
from django.forms.widgets import Textarea, RadioSelect, CheckboxInput
from images.models import Image
from links.models import Link
from .models import Artist

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

class ArtistForm(forms.ModelForm):

    image = CustomModelChoiceField(
        queryset=Image.objects.all(),
        help_text=Artist._meta.get_field('image').help_text,
    )
    
    class Meta:
        model = Artist 

        fields = [
            'name',
            'slug',
            'home_town',
            'image',
            'links',
            'statement',
            'media',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ArtistForm, self).__init__(*args, **kwargs)
        self.fields['image'].queryset = Image.objects.filter(
            user=user,
        ).order_by(
            '-creation_date',
        )
        self.fields['links'].queryset = Link.objects.filter(
            user=user,
        ).order_by(
            '-creation_date',
        )

