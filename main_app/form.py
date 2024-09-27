from django import forms


class ClientForm(forms.Form):
    name = forms.CharField(label='name',
                           max_length= 50,
                           )
    phone = forms.CharField(label='phone',
                            max_length=12,
                            )