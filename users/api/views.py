from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.api.serializers import RegistrationSerializer, EmailSerializer
from users.views import OTP
from rest_framework import serializers
from rest_framework import generics
from rest_framework.parsers import JSONParser
from users.models import CustomUser
from projectII.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings



@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        print('asd')
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


class PasswordResetAPI(generics.ListCreateAPIView):
    serializer_class = EmailSerializer
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        cmd = request.query_params.get('cmd')
        print('post')
        if cmd == 'password_reset':
            print(cmd)
            request.session['OTP'] = OTP(6)
            request.session.set_expiry(600)
            request_data = request.data
            email = request_data['email']
            request.session['email'] = email
            host = request.get_host()
            url = 'password_reset_confirm'
            try:
                    account = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                print(email + '111')
                raise serializers.ValidationError('Email "%s" does not exist.' % email)
            print(request_data)
            print(request.get_host())
            subject = 'TH'
            recepient = request_data['email']
            content = host + '/' + url + '/?cmd=password_reset_confirm&otp=' + request.session['OTP']
            print(content)

            send_mail(subject, content, EMAIL_HOST_USER, [recepient], fail_silently=False)
            return JsonResponse({'status': 200, 'OTP': request.session['OTP']})
        if cmd == 'password_reset_confirm':
            print(cmd)
            token = request.query_params.get('otp')
            print(token)
            print(request.session['OTP'])
            request_data = request.data
            user = CustomUser.objects.filter(email=request.session['email']).first()
            password = request_data['password']
            password2 = request_data['password2']
            if password != password2:
                raise serializers.ValidationError('Password not match')
            user.set_password(password)
            user.save()
            del request.session['OTP']
            return Response({'status': 'ok'})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'done': 1})





