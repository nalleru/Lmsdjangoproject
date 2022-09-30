from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView
'''CourseListView, CourseDetailView, LessonDetailView, SearchView, create_course, create_topic, create_lesson'''

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    '''
    path('courses/<int:category>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='search-courses'),
    path('create/course', create_course, name='create_course'),
    path('create/topic', create_topic, name='create_topic'),
    path('create/lesson', create_lesson, name='create_lesson'),
    '''
]