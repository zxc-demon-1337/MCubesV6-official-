from django.contrib import admin
from .models import Solve

@admin.register(Solve)
class SolveAdmin(admin.ModelAdmin):
    list_display = ['user', 'cube_type', 'formatted_time', 'solved_at', 'scramble']
    list_filter = ['cube_type', 'solved_at', 'user']
    search_fields = ['user__username', 'scramble']
    readonly_fields = ['solved_at']
    
    def formatted_time(self, obj):
        return obj.formatted_time()
    formatted_time.short_description = 'Время'