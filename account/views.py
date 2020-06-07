from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.serializers import RegistrationSerializer


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        print(serializer.is_valid())
        if serializer.is_valid():

            user = serializer.save()
            print(user)
            data['response'] = "Новый пользователь успешно зарегистрирован."
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
        else:
            print('----------------')
            data = serializer.errors
        return Response(data)
