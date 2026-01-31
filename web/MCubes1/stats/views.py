from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rubik_timer.models import Solve

@login_required
def history_view(request):
    """Страница истории всех сборок пользователя"""
    solves = Solve.objects.filter(user=request.user).order_by('-solved_at')
    
    return render(request, 'stats/history.html', {
        'solves': solves,
    })