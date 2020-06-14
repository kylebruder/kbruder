from django import forms
from templates.widgets import ImagePreviewWidget
from .models import Image, Gallery, Piece

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


class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = [
            'title',
            'image_file',
            'caption',
            'credit',
        ]
        widgets = {
            'image_file': ImagePreviewWidget
        }
        help_texts = {
            'title': "Give the image a memorable and unique title that will be easy to reference later.",
            'image_file': "Obtain permission before uploading depicitons of private persons or places. Image Preview will appear when successfully uploaded.",
            'caption': "Captions may appear on pages that include Images or other objects that use Images",
            'credit': "Give credit to the original creator of the image file. Obtain expressed permission before uploading images with exclusive rights.",
        }

class ImageUpdateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = [
            'title',
            'caption',
            'credit',
        ]
        widgets = {
            'image_file': ImagePreviewWidget
        }
        help_texts = {
            'title': "Give the image a memorable and unique title that will be easy to reference later.",
            'caption': "Captions may appear on pages that include Images or other objects that use Images",
            'credit': "Give credit to the original creator of the image file. Obtain expressed permission before uploading images with exclusive rights.",
        }

class GalleryForm(forms.ModelForm):

    cover_image = CustomModelChoiceField(
        queryset=Image.objects.all(),
        required=True,
        help_text=Gallery._meta.get_field('cover_image').help_text,
    )

    pieces = CustomModelMultipleChoiceField(
        queryset=Piece.objects.all(),
        required=True,
        help_text=Gallery._meta.get_field('pieces').help_text,
    )

    class Meta:
        model = Gallery

        fields = [
            'title',
            'slug',
            'caption',
            'cover_image',
            'pieces',
        ] 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['cover_image'].queryset = Image.objects.filter(
            user=user,
        ).order_by(
            '-creation_date',
        )
        self.fields['pieces'].queryset = Piece.objects.filter(
            user=user,
        ).filter(
            is_public=True,
        ).order_by(
            '-publication_date',
        )

class PieceForm(forms.ModelForm):

    class Meta:
        model = Piece

        fields = [
            'slug',
            'image',
            'detail_images',
            'description',
            'number',
            'artists',
            'year',
            'collection',
            'length',
            'length_unit',
            'width',
            'width_unit',
            'depth',
            'depth_unit',
            'mass',
            'mass_unit',
            'price',
            'currency',
            'is_sold',
            'contact_email',
            'contact_name',
            'contact_link',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PieceForm, self).__init__(*args, **kwargs)
        self.fields['image'].queryset = Image.objects.filter(
            user=user,
        ).order_by(
            '-creation_date',
        )
        self.fields['detail_images'].queryset = Image.objects.filter(
            user=user,
        ).filter(
            is_public=True,
        ).order_by(
            '-creation_date',
        ) 
