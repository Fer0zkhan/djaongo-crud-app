from django import forms
from .models import ClientUsers


class ClientUsersForm(forms.ModelForm):
    class Meta:
        model = ClientUsers
        fields = '__all__'
