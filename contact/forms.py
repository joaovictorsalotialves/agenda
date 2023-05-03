from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Digite seu nome',
            },
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            msg_error = ValidationError(
                'Primeiro nome, não pode ser ABC',
                code='invalid'
            )
            self.add_error('first_name', msg_error)

        return first_name
