from django.urls import path
from . import views

urlpatterns = [
    path("checkin/profile/", views.profile, name="checkin_profile"),
    path("checkin/progress/", views.progress, name="checkin_progress"),
    path("checkin/submit/", views.submit, name="checkin_submit"),
    path("checkin/leaderboard/", views.leaderboard, name="checkin_leaderboard"),
    path("checkin/export/", views.export_csv, name="checkin_export"),
]
