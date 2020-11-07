from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework_jwt.settings import api_settings
from accounts.api.serializers import UserSerializer
from rest_framework import generics
from accounts.api.serializers import RegistrationSerializer
from accounts.models import Account
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='./account.log', level=logging.DEBUG)


class RegistrationView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        logger.debug(request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Пользователь успешно зарегистрирован.'
            data['email'] = account.email
            data['username'] = account.username
            data['registered'] = True
            status = 201
        else:
            data = {'registered': False, 'reason': serializer.error_messages}
            logger.debug(data)
            status = 406
        return Response(data, status=status)


class UserList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer


class UserLogin(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        if username is None:
            return Response({'error': 'Введите логин'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = Account.objects.get(username=username)
            if not user.check_password(request.data['password']):
                return Response({'error': 'Неверный пароль'}, status=status.HTTP_400_BAD_REQUEST)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({"token": token, "user": UserSerializer(user,
                                                                    context={'request': request}).data},
                            status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_403_FORBIDDEN)