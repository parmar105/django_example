from django import forms
from .models import UsersInfo


class UserForm(forms.ModelForm):
    class Meta:
        model = UsersInfo
        fields = "__all__"