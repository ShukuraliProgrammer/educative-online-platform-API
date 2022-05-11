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
class IsUserAdmin(UserAdmin):
    list_display = ("id", "username", "first_name", "last_name", "email", "is_staff")
    list_filter = ("is_staff", )
    readonly_fields = ["username", "first_name", "last_name", "email"]

