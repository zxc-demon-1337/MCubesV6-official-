from django import forms
from .models import Solve

class SolveForm(forms.ModelForm):
    class Meta:
        model = Solve
        fields = ['cube_type', 'scramble', 'solve_time']
        widgets = {
            'scramble': forms.HiddenInput(),
            'solve_time': forms.HiddenInput(),
            'cube_type': forms.HiddenInput(),
        }