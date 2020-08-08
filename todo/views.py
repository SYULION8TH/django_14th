from .models import Todo
from rest_framework import generics
from .serializers import TodoSerializer

class TodoListGenerics(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer