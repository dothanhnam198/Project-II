from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from client.forms import RegistrationForm


class LoginView(TemplateView):

    def get(self, request, *args, **kwargs):
        response = TemplateResponse(request, 'auth/login.html', {
        })

        return response

    def post(self, request):
        username = self.request.POST['username']
        password = self.request.POST['password']
        redirect_url = self.request.GET['next']

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(redirect_url)
        else:
            return TemplateResponse(self.request, 'auth/login.html', {

            })


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'auth/register.html', context)
