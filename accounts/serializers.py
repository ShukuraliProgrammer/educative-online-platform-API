from rest_framework import serializers
from accounts.models import StudentUser, TeacherUser


class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ('user', 'full_name', 'avatar')

    def create(self, validated_data):
        if validated_data['email'] is None:
            user = ValueError
        else:
            user = StudentUser.objects.create(**validated_data)
        return user


class UserCredentialsSerialzier(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherUser
        fields = ('user', 'full_name', 'is_approve')
