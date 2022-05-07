from .models import Utilisateur
from django import forms
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('email','username','first_name','last_name','password','phone_number','address','birthday','photo','Cv','nom_entreprise','domaine')
