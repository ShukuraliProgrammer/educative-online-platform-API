from django.contrib import admin
from accounts.models import StudentUser, TeacherUser, User
from django.contrib.auth.admin import UserAdmin


@admin.register(TeacherUser)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_approve')
    search_fields = ('full_name',)


@admin.register(StudentUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'type')
    search_fields = ('username',)
