from database.models import Lesson
from django.shortcuts import render, redirect


def lesson_view(request):
    context = {}
    list = Lesson.objects.filter(teacher_id=request.user.id)
    context['lessons'] = list
    return render(request, 'teacher/lesson_view.html', context)