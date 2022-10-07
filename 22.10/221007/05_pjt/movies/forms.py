from django import forms
from .models import Movie
from django.contrib.admin import widgets

class MovieForm(forms.ModelForm):
    genre=forms.ChoiceField(
        choices=[('코미디','코미디'),('공포','공포'),('로맨스','로맨스')], 
        widget = forms.Select()
        )
    score=forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step':0.5,
                'min':0,
                'max':5
            }
        )
    )
    release_date=forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'})
    )

    class Meta:
        model=Movie
        exclude=['author']
