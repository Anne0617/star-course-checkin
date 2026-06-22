from django.contrib import admin
from .models import StarCheckinScore

@admin.register(StarCheckinScore)
class StarCheckinAdmin(admin.ModelAdmin):
    list_display = ("user", "day_number", "score", "hp_left", "completed_at")
    list_filter = ("day_number", "completed_at")
    search_fields = ("user__username", "user__last_name")
    date_hierarchy = "completed_at"
