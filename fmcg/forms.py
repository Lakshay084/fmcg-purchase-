from django import forms
from .models import Tender

class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['product_name', 'quantity', 'rate_per_tonne']
