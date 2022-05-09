from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from accounts.permissions import IsTeacher, IsStudent
from rest_framework.permissions import (
    IsAuthenticated,IsAuthenticatedOrReadOnly,
    IsAdminUser
)
from accounts.permissions import IsStudent, IsTeacher
from rest_framework.views import APIView
from courses.models import (
    Category, Course, Rating,
    Video, ContentOfCourse, Cart, Order
)
from courses.serializers import (
    CourseSerializer, RatingSerializer,
    CategoryListCreateSerializer, CategoryRetrieveSerialzier,
    VideoSerializer, CourseContentCreateSerializer, AdminDashboardSerializer,
    CartListSerializer, CartCreateDetailSerializer, CreateOrderSerializer, ListOrderSerializer
)
from accounts.models import TeacherUser, StudentUser
from accounts.serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class UnApprovedTeacherAPI(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = TeacherUser.objects.filter(is_approve=False)
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]


class AdminDashboardAPI(ListAPIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = AdminDashboardSerializer
    filter_backends = [DjangoFilterBackend]


class TeacherDashboardAPI(ListCreateAPIView):
    permission_classes = [IsTeacher, IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    def get_queryset(self):
        teacher_ids = self.request.user.id
        courses = self.queryset.filter(teacher_id=teacher_ids)
        return courses


class CategoryListCreateAPI(ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Category.objects.all()
    serializer_class = CategoryListCreateSerializer
    filterset_fields = ['title', ]

class CategoryRetrieveUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerialzier


class CourseListAPI(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ['title', 'teacher', 'category']

class CourseRetrieveAPI(RetrieveAPIView):
    permission_classes = [IsStudent, IsAuthenticated, IsTeacher]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class VideoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsTeacher, IsAuthenticated, IsAdminUser]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetrieveUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CreateRatingforCourseAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def filter_queryset(self, queryset):
        queryset = self.queryset.filter(course_id=self.kwargs['pk'])
        return queryset


class RetrieveRatingforCourseAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsTeacher,IsAdminUser]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    # def get_queryset(self):
    #     rating = self.queryset.filter(course=self.kwargs['pk'])
    #     print(rating)
    #     return rating


class CourseContentCreateAPI(ListCreateAPIView):
    permission_classes = [IsTeacher]
    queryset = ContentOfCourse.objects.all()
    serializer_class = CourseContentCreateSerializer


class StudentCourseAPI(ListAPIView):
    permission_classes = [IsStudent]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CartListCreateAPI(ListCreateAPIView):
    permission_classes = [IsStudent,IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CartCreateDetailSerializer
        else:
            return CartListSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [IsStudent,IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data["courses"])
        serializer.save(user=self.request.user.studentuser, price=10)

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = ListOrderSerializer
    permission_classes = [IsAuthenticated,IsStudent]

    def get_queryset(self):
        orders = self.queryset.filter(user=self.request.user.id)
        return orders

