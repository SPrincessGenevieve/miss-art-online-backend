from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # You can specify the fields you want

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')

        # Set the price based on the selected category
        if category == 'Head Shot':
            cleaned_data['price'] = 5
        elif category == 'Bust Up':
            cleaned_data['price'] = 10
        elif category == 'Half Body':
            cleaned_data['price'] = 15
        elif category == 'Full Body':
            cleaned_data['price'] = 20
        elif category == 'Personalize':
            custom_price = cleaned_data.get('custom_price')
            cleaned_data['price'] = custom_price if custom_price else 0  # Set default to 0 if no custom price is provided

        return cleaned_data
