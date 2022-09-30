from django.shortcuts import render
import secrets
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from courses.models import Topic, Lesson, Course
from memberships.models import UserMembership
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CourseForm, TopicForm, LessonForm


# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Course.objects.all()
        context['category'] = category
        return context
