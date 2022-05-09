from rest_framework import serializers
from courses.models import (
    Course, Video, Rating,
    Category, ContentOfCourse,
    Cart, Order
)
from accounts.serializers import TeacherSerializer


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'v_url', 'v_file', 'mode')


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    video_url = VideoSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('title', 'description', 'teacher','video_url', 'difficulty', 'duration', 'number_of_student','created', 'updated')


class CategoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class CategoryRetrieveSerialzier(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'course',)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'course', 'rating', 'comment')


class CourseContentCreateSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = ContentOfCourse
        fields = ('title', 'course', 'video', 'mode')


class AdminDashboardSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'teacher', 'number_of_student')


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'course')


class CartCreateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'course')


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("courses",)

class ListOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
