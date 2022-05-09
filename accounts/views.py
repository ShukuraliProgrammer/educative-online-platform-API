from django.shortcuts import render, get_object_or_404
from rest_framework import mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)
from accounts.permissions import IsStudent, IsTeacher
from accounts.serializers import (
    UserCredentialsSerialzier, StudentUserSerializer,
    TeacherSerializer,
)
from accounts.models import StudentUser, TeacherUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView, ListCreateAPIView,
    RetrieveAPIView,RetrieveUpdateDestroyAPIView
)


class StudentUserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,IsStudent]
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset
        user = get_object_or_404(queryset,pk=kwargs['pk'])
        serializer = self.serializer_class(user )
        return Response(serializer.data)

class TeacherListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherSerializer

class UserTokenViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = UserCredentialsSerialzier

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = StudentUser.objects.filter(email=email)
            if not user.exists():
                return Response({
                    "detail": "User does not exist"
                })

            user = user.first()

            if not user.check_password(password.strip()):
                return Response({
                    "detail": "Wrong credentials"
                })

            token = Token.objects.create(user=user)

            return Response({
                "token": str(token.key)
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

