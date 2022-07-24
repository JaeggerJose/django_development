from django.shortcuts import render
from django.views.generic import View
from .base_render import render_to_response

# Create your views here.

class Index(View):
    def get(self, request):
        data = { 'name':'mike', 'id':21 }
        return render_to_response(request, 'index.html', data=data)