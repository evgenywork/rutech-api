from rest_framework import serializers
from account.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        from datetime import datetime

        # current date and time
        now = datetime.now()
        user = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],


            # email="test" + str(datetime.timestamp(now)) + "@",
            # first_name=self.validated_data['first_name'],
            # last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],

        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Пароли должны совпадать'})
        user.set_password(password)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'job_title', 'avatar', 'is_admin', 'is_guest', 'is_investor', 'is_startup', 'is_user', 'tags')


class UserAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'avatar', 'is_admin', 'is_guest', 'is_investor', 'is_startup', 'is_user',
                  'job_title', 'firma_name', 'tags')