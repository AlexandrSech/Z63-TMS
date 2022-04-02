from django import forms
from .models import Person


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields =["firstname", "lastname", "age", "profession"]
