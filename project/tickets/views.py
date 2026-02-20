from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

#1 without rest framework 

def no_rest_module(requesr) : 
    guests = [
        {
            'id' : 1 , 
            'Name' : 'omar',
            "mobile" : 789099,
        },
         {
            'id' : 2 , 
            'Name' : 'zino',
            "mobile" : 569099,
        }
    ]
    return JsonResponse(guests , safe=False)