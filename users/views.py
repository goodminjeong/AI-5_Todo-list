from users.models import User
from users.serializers import UserInfoSerializer, UserSerializer, CustomTokenObtainPairSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class SignupView(APIView):
    def post(self, request):
        """회원가입"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def get(self, request, user_id):
        """회원정보 보기"""
        user = get_object_or_404(User, id=user_id)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def put(self, request, user_id):
        """회원정보 수정"""
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            serializer = UserInfoSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "수정 권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)

    @permission_classes([IsAuthenticated])
    def delete(self, request, user_id):
        """회원탈퇴"""
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            request.user.delete()
            return Response({"message": "회원탈퇴가 완료되었습니다"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_403_FORBIDDEN)


class CustomTokenObtainPairView(TokenObtainPairView):
    """페이로드 커스터마이징"""
    serializer_class = CustomTokenObtainPairSerializer
