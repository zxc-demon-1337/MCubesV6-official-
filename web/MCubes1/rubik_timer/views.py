import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Solve
from .forms import SolveForm

def generate_2x2_scramble():
    """Генерирует случайную формулу для кубика 2х2"""
    moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
    scramble = []
    prev_move = None
    
    for _ in range(9):
        move = random.choice(moves)
        while prev_move and move[0] == prev_move[0]:
            move = random.choice(moves)
        scramble.append(move)
        prev_move = move
    
    return ' '.join(scramble)

# @login_required
# def timer_view(request):
#     initial_scramble = generate_2x2_scramble()
    
#     if request.method == 'POST':
#         form = SolveForm(request.POST)
#         if form.is_valid():
#             solve = form.save(commit=False)
#             solve.user = request.user
#             solve.save()
#             return redirect('rubik_timer:timer')
#     else:
#         form = SolveForm(initial={
#             'scramble': initial_scramble,
#             'cube_type': '2x2'
#         })
    
#     return render(request, 'rubik_timer/timer.html', {
#         'form': form,
#         'scramble': initial_scramble,
#     })

@login_required
def timer_view(request):
    if request.method == 'POST':
        form = SolveForm(request.POST)
        if form.is_valid():
            solve = form.save(commit=False)
            solve.user = request.user
            solve.save()
            return redirect('rubik_timer:timer')

    scramble = generate_2x2_scramble()
    form = SolveForm()
    return render(request, 'rubik_timer/timer.html', {
        'scramble': scramble,
        'form': form
    })
