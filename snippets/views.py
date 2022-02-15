from ast import Delete
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User 
from rest_framework import permissions


class UserList(generics.ListAPIView):
    permision_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    permision_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer



class SnippetList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



# class SnippetList(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
    
# ):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class SnippetDetail(
#     mixins.DestroyModelMixin, 
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin, 
#     generics.GenericAPIView
# ):

#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


#     def get(self, request, *args, **kwargs):

#         print(kwargs['pk'])
#         return self.retrieve(self, *args, **kwargs )

#     def put(self, request, *args, **kwargs):
#         return self.update(self, *args, **kwargs )

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(self, *args, **kwargs )


# class SnippetList(APIView):

#     def get(self, request, format = None):

#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data)

    
#     def post(self, request, format = None ):
#         serializer =    SnippetSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        



# class SnippetDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk = pk)
#         except Snippet.DoesNotExist:
#             raise Http404 
    

#     def get(self, request, pk, format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    

#     def put(self, request, pk,  format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     def delete(self, request, pk, format = None):

#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
    


        






# # Create your views here.
# @api_view(['GET', 'POST'])
# def snippet_list(request, format = None):

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         # return JsonResponse(serializer.data,  safe = False)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         # return JsonResponse(serializer.errors,  status = 400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format = None):

#     try:
#         snippet = Snippet.objects.get(pk = pk)
#     except Snippet.DoesNotExist:
#         # return HttpResponse(status = 404)
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         # return JsonResponse(serializer.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
    
#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data)
#             return Response(serializer.data, )
        
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)