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
        Client.objects.update_or_create(
            name = request.POST['name'],
            phone = request.POST['phone'],
            agreement = request.POST['agreement'],
        )
        return redirect('/')


class Policy(View):
    def get(self, request):
        return render(request,
                      'main_app/policy.html'
                      )
    
class About(View):
    def get(self, request):
        return render(request,
                      'main_app/about.html',
                      )
    
class Discounts(View):
    def get(self, request):
        return render(request,
                      'main_app/discount.html',
                      )
    
class Contacts(View):
    def get(self, request):
        return render(request,
                      'main_app/discount.html',
                      )
    
class Personal_data(View):
    def get(self, request):
        return render(request,
                      'main_app/personal_data.html'
                      )