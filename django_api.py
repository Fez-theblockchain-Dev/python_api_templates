from django.db import models
from rest_framework import status, serialization
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django_api import UserSerializer, routers, viewsets, action



@api_view(["GET", "POST"])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view("GET", "EDIT")    
class User(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_user_info(self, user_info, ):
        
        self.get_user_info = user_info
        try:
            user_info is not None
            return(user_info)
        except:
            return("User not found. Please try the api call again.")
        
# This class defines how the user views from the forum will look on the database querying side. 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   
# Routers provide an easy way of automatically determining the URL conf.
    router = routers.DefaultRouter()
    router.register(r"users", UserViewSet)

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        if request.method == "GET":
            snippet = self.get_object()
            serializer = SnippetSerializer(snippet)
            return Response(serializer.data)

    def update(self, request, pk=None):
        if request.method == "PUT":
            snippet = self.get_object()
            serializer = SnippetSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        if request.method == "PATCH":
            snippet = self.get_object()
            serializer = SnippetSerializer(snippet, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if request.method == "DELETE":
            snippet = self.get_object()
            snippet.delete()
            return Response("The data was successfully deleted!", status=status.HTTP_204_NO_CONTENT)
    

