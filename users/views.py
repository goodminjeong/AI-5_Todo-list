from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

# Create your views here.


class SignupView(APIView):
    def post(self, request):
        """회원가입"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        response = Response({
            "message": "로그아웃 되었습니다"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('refreshtoken')
        response.delete_cookie('accesstoken')
        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    """payload customizing"""
    serializer_class = CustomTokenObtainPairSerializer
