from django import forms  
from .models import Publication  
class PublicationForm(forms.ModelForm):  
    class Meta:  
        model = Publication  
        fields = ('titre','description','domaine','periode') 