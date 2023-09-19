from django import forms

from shopapp.models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=100000)
#     description = forms.CharField(widget=forms.Textarea, label="Description")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"
