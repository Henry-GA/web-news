from django import forms
from tinymce import TinyMCE

from web.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
