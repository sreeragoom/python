from django import forms
from .models import Players


class PlayerForm(forms.ModelForm):
    class Meta:
        model=Players
        fields=['name','age','desc','market_value','img','position']