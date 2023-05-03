from django.shortcuts import render, get_object_or_404

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


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )
