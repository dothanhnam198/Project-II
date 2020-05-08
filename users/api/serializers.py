from rest_framework import serializers
from users.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2', 'email']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        account = CustomUser(
            username=self.validated_data['username'],
            email =self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        account.set_password(password)
        account.save()
        return account


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email',)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                print(email + '1')
                raise serializers.ValidationError('Email "%s" does not exist.' % email)
            return email

