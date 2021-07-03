from django.http import request
from django.shortcuts import render
from django.views.generic.base import View
from core import models

class LiveView(View):

    def get(self, request):
        settings = models.Settings.objects.first()
        return render(request, "live/index.html", {"settings": settings})
    
