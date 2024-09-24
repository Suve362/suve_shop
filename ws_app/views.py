from django.shortcuts import render
from django.views.generic import TemplateView


class WSView(TemplateView):
    template_name = '/opt/python_projects/suve_shop/ws_app/templates/ws_app.html'
