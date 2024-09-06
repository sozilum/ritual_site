from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from .models import Client

class Homepage(View):

    def get(self, request):
        return render(request, 
                      'main_app/homepage.html',
                      )
    
    def post(self, request):
        print(request.body)
        
        return redirect('/')

class Policy(View):
    
    def get(self, request):
        return render(request,
                      'main_app/policy.html'
                      )