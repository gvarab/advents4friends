from django import forms
from tinymce.widgets import TinyMCE
from .models import Door


class DoorForm(forms.ModelForm):

    class Meta:
        model = Door
        fields = ['content', ]
        widgets = {
            'content': TinyMCE(),
        }

