from django import forms
from .models import Contatto

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = '__all__'