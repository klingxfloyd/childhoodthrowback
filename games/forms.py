from django import forms
from .models import PANTSGame


class PANTSForm(forms.ModelForm):

    place = forms.CharField(label='Place', max_length=300,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Name of Places'}))

    animal = forms.CharField(label='Animal', max_length=300,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Name an Animal'}))
    name = forms.CharField(label='Name', max_length=300,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Type a Name'}))
    thing = forms.CharField(label='Thing', max_length=300,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Name a Thing'}))

    class Meta:
        model = PANTSGame
        fields = ['place', 'animal', 'name', 'thing']