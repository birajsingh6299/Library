from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Books
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BooksSerializer
from Library import serializers

# Create your views here.

def homepage(request):
    return render(request,'Homepage.html')

@api_view(['GET'])
def Book_view(request):
    view=Books.objects.all()
    serializer=BooksSerializer(view,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Book_update(request, id):
    update=Books.objects.get(id=id)
    serializer=BooksSerializer(instance=update, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Book_create(request):
    is_staff=request.user.is_staff
    if is_staff==1:
        serializer=BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('No authorisation to create book')
    
@api_view(['DELETE'])
def Book_delete(request, id):
    is_staff=request.user.is_staff
    if is_staff==1:
        delete=Books.objects.get(id=id)
        delete.delete()
        return Response('Book deleted Successfully')
    else:
        return Response('No authorisation to delete the book')

@api_view(['POST'])
def Book_update(request, id):
    is_staff=request.user.is_staff
    if is_staff==1:
        update=Books.objects.get(id=id)
        serializer=BooksSerializer(instance=update, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('No Authorisation to update the books')

@api_view(['POST'])
def Book_return(request, id):
    return_bk=Books.objects.get(id=id)
    if return_bk.status=='borrowed':
        return_bk.status='available'
        data={'status':return_bk.status}
        serializer=BooksSerializer(instance=return_bk, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response('Status Updated')
        return Response(serializer.data)
    else:
        return Response('Book is already available')

@api_view(['POST'])
def Book_borrow(request, id):
    borrow=Books.objects.get(id=id)
    if borrow.status=='available':
        borrow.status='borrowed'
        data={'status':borrow.status}
        serializer=BooksSerializer(instance=borrow, data=data, partial=True)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response('Status Updated')
        return Response(serializer.data)
    else:
        return Response('Book is unavailable') 


    














