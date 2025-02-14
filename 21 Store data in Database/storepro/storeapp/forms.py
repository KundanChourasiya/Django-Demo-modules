from django import forms
from .models import ProductData

class ProductForm(forms.Form):
    productname=forms.CharField(
        label='Enter Product Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )

    productcost=forms.IntegerField(
        label='Enter Product Cost',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

    productcolor=forms.CharField(
        label='Enter Product Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )

    productdesc=forms.CharField(
        label='Enter Product Description',
        help_text='please enter 100 text',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Desc'
            }
        )
    )