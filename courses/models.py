from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-category. {self.title}"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("created", "updated")


class Course(models.Model):
    class DifficultyDegree(models.TextChoices):
        easy = "Easy", _("Easy")
        medium = "Medium", _("Medium")
        difficult = "Difficult", _("Difficult")

    category = models.ForeignKey('courses.Category', on_delete=models.SET_NULL, related_name='courses', null=True,
                                 blank=True)
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    teacher = models.ForeignKey('accounts.TeacherUser', on_delete=models.CASCADE, related_name='courses')
    difficulty = models.CharField(_("Difficulty Degree of Course"), choices=DifficultyDegree.choices, max_length=100)
    duration = models.CharField(_("Duration of Course"), max_length=200)
    number_of_student = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.teacher}"

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ('created',)


class Video(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    v_url = models.URLField(_("Video url"), null=True, blank=True)
    v_file = models.FileField(_("Video file"), upload_to='media/video')
    mode = models.IntegerField(_("To sort Videos"))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        ordering = ("mode",)


class Rating(models.Model):
    user = models.ForeignKey('accounts.StudentUser', on_delete=models.CASCADE, related_name='ratings')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(_("Stars given"))
    comment = models.TextField(_("Comment"))

    def __str__(self):
        return f"{self.rating} stars to {self.course}"

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
        ordering = ('rating',)


class ContentOfCourse(models.Model):
    title = models.CharField(_("Title"), max_length=80)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, related_name='courses')
    video = models.ManyToManyField('courses.Video')
    mode = models.IntegerField(_("To sort Content"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Course Content")
        verbose_name_plural = _("Course Contents")
        ordering = ('mode',)


class Cart(models.Model):
    user = models.ForeignKey('accounts.StudentUser', on_delete=models.CASCADE, related_name='carts_user')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='carts_course')

    def __str__(self):
        return f"{self.id}-cart of {self.user}"

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")
        unique_together = ('user', 'course')


class Order(models.Model):
    class PayStatus(models.TextChoices):
        created = "created", _("Created")
        paid = "paid", _("Paid")

    user = models.ForeignKey('accounts.StudentUser', on_delete=models.CASCADE, related_name='orders')
    courses = models.ManyToManyField('courses.Course')
    price = models.BigIntegerField(_("Price"))
    status = models.CharField(_("Status of Order"), max_length=64, choices=PayStatus.choices,
                              default=PayStatus.created.value)

    def __str__(self):
        return f"{self.user} ordered to {self.courses}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class AcquiredKnowledge(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    is_done = models.BooleanField(_("Is Done"), default=False)
    mode = models.IntegerField(_("To sort "))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Acquired Knowledge")
        verbose_name_plural = _("Acquired Knowledges")
        ordering = ("created",)


class Requirment(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    is_done = models.BooleanField(_("IIs Done"), default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Requirement")
        verbose_name_plural = _("Requirements")
        ordering = ('created',)


class ToWhom(models.Model):
    title = models.CharField(_("Title"), max_length=80)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("For Whom")
        verbose_name_plural = _("For Whom")
