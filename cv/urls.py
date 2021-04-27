from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from . import views

urlpatterns = [
    path("", views.MainTemplate.as_view()),

]
