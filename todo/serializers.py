from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer): # Model을 바탕으로 Serializer를 작성하겠다.
    class Meta: # class 보조적인 정보를 전달할 때 이용합니다.
        model = Todo # 데이터를 serializer 해서 만들려는 모델 
        fields= ['done', 'created_date', 'todo', 'due_date'] # 현재 model에 있는 모든 필드를 가져온다.