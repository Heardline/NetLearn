from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Token
from .serializers import TokenSerializer, LoginSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response(TokenSerializer(token).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        # Remove token to log user out
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
