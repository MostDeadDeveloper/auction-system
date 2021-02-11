from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.conf import settings


class BaseRedirectView(TemplateView):

    def get_template_names(self):
        template_name = 'index.html'
        return template_name
