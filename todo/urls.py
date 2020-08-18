from django.urls import path, include # include를 추가
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('todo/', views.TodoListAPIView.as_view()), # 라우터에 등록된 url들을 include 해준다.
    path('todo/<int:pk>/', views.TodoDetailAPIView.as_view()), # 라우터에 등록된 url들을 include 해준다.
]

urlpatterns = format_suffix_patterns(urlpatterns)