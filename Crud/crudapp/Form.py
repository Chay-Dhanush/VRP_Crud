


from django import forms
from .models import OrderModel


class OrderForm(forms.ModelForm):
    class Meta:
        model=OrderModel
        fields='__all__'
        Laptop_Choices=[
        ('Asus Laptop','Asus Laptop'),('Leonovo Laptop','Leonovo Laptop'),('Dell Laptop','Dell Laptop'),('Hp Laptop','Hp Laptop'),('Acer Laptop','Acer Laptop')]

        widgets={
            'ProductId':forms.NumberInput(attrs={'placeholder':'eg.100'}),
            'CustomerName':forms.TextInput(attrs={'placeholder':'eg.Dhanush P'}),
            'Product':forms.Select(attrs={'placeholder':'eg. select your Laptop'},choices=Laptop_Choices),
            'ProductPrice':forms.NumberInput(attrs={'placeholder':'eg.30000'}),
            'CustomerPhone':forms.NumberInput(attrs={'placeholder':'eg.9790511323'}),
            'CustomerEmail':forms.EmailInput(attrs={'placeholder':'dhanush@gmail.com'}),
            'CustomerAddress':forms.TextInput(attrs={'placeholder':'eg.40,Bajanai kovil Street, Pasur, Annur'}),
            'State':forms.TextInput(attrs={'placeholder':'Tamil Nadu'})
        }