from django.shortcuts import render
from django.http.response import JsonResponse
from tickets.models import Guest , Movie , Reservation
# Create your views here.

#1 without rest framework 

def no_rest_module(request):
    guests = [
        {
            'id': 1, 
            'name':'anonymos',
            'mobile':78278, 
        },
        {
            'id': 2, 
            'name':'anonymos2',
            'mobile':78278, 
        }
    ]
    return JsonResponse(guests , safe=False)


#2 model data defalut without rest 

def from_module(request) : 
    data = Guest.objects.all()
    response = {
        'guests' : list(data.values('name' , 'mobile'))
    }
    return JsonResponse(response)