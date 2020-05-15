from database.models import Score
from django.shortcuts import render, redirect


def score_view(request):
    context = {}
    list = Score.objects.filter(student_id=request.user.id)
    context['score'] = list
    return render(request, 'student/score_list.html', context)