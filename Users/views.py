from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer
from Users import serializers

# Create your views here.

class UserAPIView(RetrieveAPIView):
    permission_classes=(IsAuthenticated)
    serializer_classes=(UserSerializer)
    def get_object(self):
        return self.request.user

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html')
    else:
        return render('login.html')


def register(request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        is_staff=0
        first_name=request.POST['Firstname']
        last_name=request.POST['Lastname']
        username=request.POST['Username']
        email=request.POST['Email']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        role=request.POST['Role']
        if role=='Librarian':
            is_staff=1
            group_id=2
        elif role=='Member':
            is_staff=0
            group_id=1
        if password1==password2:
            if(not User.objects.filter(username=username).exists()):
                if(not User.objects.filter(email=email).exists()):
                    user=User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name, is_staff=is_staff)
                    user.save()
                    return redirect('/')
                else:
                    messages.info(request,'Email already registered')
                    return render(request, 'register.html')
            else:
                messages.info(request,'Username already registered')
                return render(request, 'register.html')
        else:
            messages.info(request,'Password Mismatch')
            return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


@api_view(['GET'])
def User_view(request):
    view=User.objects.all()
    serializer=UserSerializer(view,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def User_update(request, id):
    is_staff=request.user.is_staff
    if is_staff==1:
        update=User.objects.get(id=id)
        serializer=UserSerializer(instance=update, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('User is not authorized')

@api_view(['DELETE'])
def User_delete(request, id):
    is_staff=request.user.is_staff
    user_id=request.user.id
    if is_staff==1 or user_id==id:
        delete=User.objects.get(id=id)
        delete.delete()
        return Response('User deleted Successfully')
    else:
        return Response('Not authorized to delete a different user')
    
        
       





