from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class User(AbstractUser):
    class TypeChoices(models.TextChoices):
        teacher = "teacher", _("teacher")
        student = "student", _("student")

    type = models.CharField(max_length=64, choices=TypeChoices.choices)

    def is_student(self):
        return hasattr(self, "studentuser")

    def is_teacher(self):
        return hasattr(self, "teacheruser")


class TeacherUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatar')
    full_name = models.CharField(max_length=100)
    is_approve = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ("-id",)

    def __str__(self):
        return f"{self.user.username}"

    def clean(self):
        if self.user.type == User.TypeChoices.student.value:
            raise ValidationError({"user": _("Bu user da Student bor")})


class StudentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='media/avatar')

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def clean(self):
        if self.user.type == User.TypeChoices.teacher.value:
            raise ValidationError({"user": _("Bu userda Teacher bor")})
