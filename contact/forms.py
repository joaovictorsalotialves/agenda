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

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro especifica',
                code='invalid',
            )
        )

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro geral',
                code='invalid',
            )
        )

        return super().clean()
