from django.shortcuts import render
from django.views.generic import TemplateView


class MainTemplate(TemplateView):
    template_name = "base.html"

