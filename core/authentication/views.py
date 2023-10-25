from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(generics.GenericAPIView):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(request.data)
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            print(user)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({"access_token": access_token})
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            raise e