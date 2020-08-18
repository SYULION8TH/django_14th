# 데이터 처리 대상 : 모델, Serializer import 시키기
from .models import Todo
from .serializers import TodoSerializer

from rest_framework import generics
from rest_framework import mixins



class TodoListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, 
                generics.GenericAPIView):
    queryset = Todo.objects.all()   # 쿼리셋 등록!
    serializer_class = TodoSerializer # Serializer 클래스 등록!

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TodoDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)