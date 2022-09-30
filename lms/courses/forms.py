from django import forms
from django.contrib.auth.models import User
from .models import Course, Topic, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['created_by',# 'slug',
                  'title', 'course', 'description']

        labels = {
            'title': 'subject title'
        }
        widgets = {'created_by': forms.HiddenInput(), #'slug': forms.HiddenInput()
         }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [#'slug',
             'title', 'topic', 'position']
'''
        widgets = {
            'slug': forms.HiddenInput()
        }
'''

