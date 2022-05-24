# Vista basada en clases
from django.shortcuts import render
from django.views.generic import View

class home_view(View):
    def get(self, request, *args, **kwargs):
        context = { }
        return render(request, 'index.html', context)


