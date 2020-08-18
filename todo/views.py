from .models import Todo
from .serializers import TodoSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class TodoListAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TodoList 클래스와는 달리 pk값을 받음 (메소드에 pk인자)
class TodoDetailAPIView(APIView):

    def get(self, request, pk, format=None):
        
        todo = self.get_object(pk)
        # post = get_object_or_404(Post, pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = PostSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)