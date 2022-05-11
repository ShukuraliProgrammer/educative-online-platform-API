from django.contrib import admin
from courses.models import (
    Category, Course, Video,
    ContentOfCourse, Rating,
    Cart, AcquiredKnowledge,
    Requirment, ToWhom,
    Order,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 10


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'teacher', 'difficulty', 'number_of_student', 'created')
    search_fields = ('category', 'title',)
    list_filter = ('teacher', 'difficulty','created', 'updated')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'comment')
    list_filter = ('user', 'course',)

# Those are simple Models

admin.site.register(Video)

admin.site.register(ContentOfCourse)

admin.site.register(Cart)

admin.site.register(Order)

admin.site.register(AcquiredKnowledge)

admin.site.register(Requirment)

admin.site.register(ToWhom)
