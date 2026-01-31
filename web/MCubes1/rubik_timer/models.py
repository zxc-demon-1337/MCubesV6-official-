from django.db import models
from django.conf import settings
from django.utils import timezone

class Solve(models.Model):
    CUBE_TYPES = [
        ('2x2', '2x2'),
        ('3x3', '3x3'),
        ('4x4', '4x4'),
        ('pyraminx', 'Пираминкс'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='solves'
    )
    cube_type = models.CharField(max_length=20, choices=CUBE_TYPES, default='2x2')
    scramble = models.CharField(max_length=200)  # формула перемешивания
    solve_time = models.FloatField()  # время в секундах
    solved_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-solved_at']
        db_table = 'rubik_timer_solve'
    
    def __str__(self):
        return f"{self.user.username} - {self.solve_time:.2f}s"
    
    def formatted_time(self):
        minutes = int(self.solve_time // 60)
        seconds = self.solve_time % 60
        return f"{minutes:02d}:{seconds:05.2f}" if minutes > 0 else f"{seconds:.2f}"