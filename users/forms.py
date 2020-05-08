from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


class EmailForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            # account = CustomUser.objects.all().get(email=email)
            # print(account)
            # if account is None:
            #     raise forms.ValidationError('Email "%s" does not exist' % email)
            try:
                account = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                print(email + '1')
                raise forms.ValidationError('Email "%s" does not exist.' % email)
                return email







