from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    passwordRepeat = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username',)

        def clean_passwordRepeat(self):
            cd = self.cleaned_data
            if cd['password'] != cd['passwordRepeat']:
                raise forms.ValidationError("Password do not match")
            return cd['passwordRepeat']
