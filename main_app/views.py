from django.views import View
from django.http import HttpResponse

from .models import Client
from .form import ClientForm


class ApiView(View):
    def post(self, request):
        
        data = request.POST
        check = ClientForm(data=data)
        
        if check.is_valid():
            # Client.objects.update_or_create(
            #     name = request.POST['name'],
            #     phone = request.POST['phone'],
            #     )
            print(data)
        else:
            raise ValueError('Что-то пошло не так, ереденны не верные данные!')
        
        return HttpResponse(status = 201)

