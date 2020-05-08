from django.shortcuts import render, HttpResponse, redirect
import random
import string
from django.core.mail import send_mail
from projectII.settings import EMAIL_HOST_USER
from . import forms
from users.forms import EmailForm
from users.models import CustomUser
from users.forms import EmailForm
from django.views.generic import TemplateView
from django.utils import timezone



# Create your views here.
def OTP(size):
    code = ''.join([random.choice(string.ascii_uppercase)
                    for n in range(size)])
    return code


def password_reset_view(request):
    context = {}
    print(timezone.now())
    print(request.session.get_expiry_age())
    return render(request, 'registration/password_reset.html', context)


def password_reset_confirm_view(request):
    context = {}
    print(request.session.get_expiry_age())
    if request.GET['otp'] != request.session['OTP']:
        return HttpResponse('Page not Found')
    context['otp'] = request.GET['otp']
    print(context)
    return render(request, 'registration/password_reset_confirm.html', context)






