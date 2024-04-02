from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].label = False  # Remove the label
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter quantity, Default 1'  # Add placeholder
        self.fields['quantity'].required = False  # Make the field not required
        self.fields['quantity'].widget.attrs['class'] = 'form-control-no-margin w-25'