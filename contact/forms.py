import re

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
            },
        ),
        label='First Name*',
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone',
            },
        ),
        help_text='(DD) 99999-9999',
        label='Phone*',
    )
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
                'required': False
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'E-mail',
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Description',
            'style': 'resize: none'
        })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg_error = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg_error)
            self.add_error('last_name', msg_error)

        return super().clean()

    def clean_phone(self):
        standard = r'(\(\d{2}\)\s|\d{2}\s)?\d{4,5}-\d{4}'
        phone = self.cleaned_data.get('phone')

        if not re.match(standard, phone):
            msg_error = ValidationError(
                'Formato de número, inválido',
                code='invalid'
            )
            self.add_error('phone', msg_error)

        return phone


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
        min_length=3,
    )

    class Meta:
        model = User
        fields = {
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        }

    def clea_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já existe usuario cadastrado com esse e-mail')
            )

        return email
