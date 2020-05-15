from database.models import Schedule, Lesson
from django.shortcuts import render, redirect


def schedule_view(request):
    context = {}
    schedule = Schedule.objects.all()
    lesson = Lesson.objects.all()
    context['schedule'] = schedule
    context['lesson'] = lesson
    return render(request, 'schedule/list.html', context)