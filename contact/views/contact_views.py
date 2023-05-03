from django.shortcuts import render
from contact.models import Contact


def index(request):
    contats = Contact.objects.all()

    context = {
        'contacts': contats,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )
