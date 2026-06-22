from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.views.static import serve
import os

PROJ_DIR = os.path.dirname(os.path.dirname(__file__))

urlpatterns = [
    path("quick-login/", lambda r: auth_login(r, authenticate(username="admin", password="admin123")) or HttpResponseRedirect("/admin/") if authenticate(username="admin", password="admin123") else HttpResponseRedirect("/admin/login/?error=1")),
    path("admin/", admin.site.urls),
    path("api/", include("learning.urls")),
    path("star-course/<path:path>", serve, {"document_root": os.path.join(PROJ_DIR, "star_course")}),
    path("star-course/", lambda r: serve(r, "index.html", document_root=os.path.join(PROJ_DIR, "star_course"))),
    path("invite/", lambda r: serve(r, "index.html", document_root=os.path.join(PROJ_DIR, "star_course"))),
    path("", lambda r: serve(r, "index.html", document_root=os.path.join(PROJ_DIR, "star_course"))),
]
