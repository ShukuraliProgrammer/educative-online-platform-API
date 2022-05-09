from django.urls import path, include
from courses.views import (
    CourseListAPI, CourseRetrieveAPI,
    RetrieveRatingforCourseAPI,
    CreateRatingforCourseAPI,
    CategoryListCreateAPI,
    CategoryRetrieveUpdateDeleteAPI,
    VideoListCreateAPI, VideoRetrieveUpdateDeleteAPI,
    CourseContentCreateAPI,UnApprovedTeacherAPI,
    AdminDashboardAPI, TeacherDashboardAPI,
    CartListCreateAPI,OrderCreateView,OrderListView,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('unapprovedteachers', UnApprovedTeacherAPI, basename='unapproved-teachers')


urlpatterns = [
    # dashboards
    path('dashboard-admin', AdminDashboardAPI.as_view(), name='admin-dashboard'),
    path('teacher/my-course/', TeacherDashboardAPI.as_view(), name='teaher-dashboard'),

    # category urls
    path('category', CategoryListCreateAPI.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDeleteAPI.as_view(), name='category-detail'),

    # course urls
    path('all/', CourseListAPI.as_view(), name='course-list'),
    path('<int:pk>/', CourseRetrieveAPI.as_view(), name='course-retrieve'),

    # rating urls
    path('<int:pk>/rating/', CreateRatingforCourseAPI.as_view(), name='course-rating-create'),
    path('<int:pk>/rating/<str:id>/', RetrieveRatingforCourseAPI.as_view(), name='course-rating'),

    # video urls
    path('video', VideoListCreateAPI.as_view(), name='video-list-create'),
    path('video/<int:pk>/',VideoRetrieveUpdateDeleteAPI.as_view(), name='video-retrieve'),

    # course content urls
    path('content', CourseContentCreateAPI.as_view(), name='content-create'),

    # cart urls
    path('cart', CartListCreateAPI.as_view(),name='cart-list-create'),


    # order urls
    path('orders/', OrderCreateView.as_view(), name="order-create"),
    path('orders/list', OrderListView.as_view(), name='order-list'),

    path('',include(router.urls))
]