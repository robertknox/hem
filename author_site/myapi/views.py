from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from myapi.serializer import UserSerializer, GroupSerializer
from django.http import HttpResponse

from django.shortcuts import render 


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def AddressInFile( request ):
    email = request.GET["email"]
    print ("Here myapi ADF: email:" + email)
    with open("email_list","a") as f:
        f.write(email + "\n")
        f.close()

    return HttpResponse("Email added to list.");

def CreateUser(request):
    email = request.GET["email"]
    firstname = request.GET["firstname"]
    lastname  = request.GET["lastname"]
    password  = request.GET["password"]
    username  = request.GET["username"]

    user = User.objects.create_user(firstname,email, password)
    user.first_name = firstname
    user.last_name  = lastname
    user.password   = password
    user.email      = email
    user.save()

    return HttpResponse("Here in CreateUser");

#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]

