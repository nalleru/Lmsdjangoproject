from django.db import models
from memberships.models import Membership
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.title)


class Topic(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    #slug = models.SlugField
    title = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    #slug = models.SlugField
    title = models.CharField(max_length=30)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.topic.slug, 'lesson_slug':self.slug})




