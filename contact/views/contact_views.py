from django.shortcuts import render
from contact.models import Contact


def index(request):
    contats = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts': contats,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )
