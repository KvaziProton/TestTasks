from django import forms

class ConvertForm(forms.Form):
    '''Input usd ammount form'''

    usd = forms.IntegerField(label='USD', min_value=0)
