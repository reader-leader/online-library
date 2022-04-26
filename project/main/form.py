from django import forms
from django.forms import ModelForm
from .models import Fanfics


class NovelForm(ModelForm):
    class Meta:
        model = Fanfics
        fields = ('title', 'author', 'category', 'description', 'status', 'genre')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-inline'}),
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'})
        }