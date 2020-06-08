from django import forms
from templates.widgets import ImagePreviewWidget
from .models import Image, Gallery, Piece

class ImageForm(forms.ModelForm):

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
