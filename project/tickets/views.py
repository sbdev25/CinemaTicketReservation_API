from django.shortcuts import render
from django.http.response import JsonResponse 
from tickets.models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .Serializers import GuestSerializer , MovieSerializer , ReservationSerializer
from rest_framework.response import Response 
from rest_framework import status

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



@api_view(['GET', 'POST'])
def FBV_List(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request , pk ) : 
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    #GET
    if request.method == 'GET' : 
        serializer = GuestSerializer(guest )
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT' : 
        serializer = GuestSerializer(guest , data = request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method == 'DELETE' : 
        guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)