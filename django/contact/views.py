from django.core.mail import mail_admins
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import ContactForm


def _send_email(context: dict):
    mail_admins(
        'New contact form response',
        render_to_string('emails/response.txt', context),
        fail_silently=False,
        html_message=render_to_string('emails/response.html', context)
    )


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            _send_email(context={
                'response': form.instance,
            })
            return HttpResponseRedirect(reverse('contact-thanks'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
