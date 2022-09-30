from django.contrib import admin
from courses.models import Topic, Lesson, Course

# Register your models here.

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(Course)
