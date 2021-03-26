from django import forms
from .models import URL_Short
from django.utils.translation import ugettext_lazy as _


class UrlForm(forms.ModelForm):

    class Meta:
        model = URL_Short
        fields = ('short_url', 'long_url')
        labels = {
            'short_url': _('Token'),
        }
        widgets = {
            'long_url': forms.TextInput(attrs=({'class': 'url-input'})),
            'short_url': forms.TextInput(attrs=({'class': 'url-input'}))
        }

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['short_url'].required = False
