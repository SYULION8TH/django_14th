from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

# Default Router 사용 X ==> API ROOT 없음. 

urlpatterns = [
    # 127.0.0.1:8000/todo == ListView
    path('todo/', views.TodoListGenerics.as_view()),  
    # 127.0.0.1:8000/todo/<pk> == DetailView
    path('todo/<int:pk>/', views.TodoDetailGenerics.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)