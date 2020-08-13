from django.db import models

# Create your models here.
class Todo (models.Model): # models.Model class를 상속받는다.
    todo = models.TextField() # 앞으로 해야할일 # 텍스트로 저장
    created_date = models.DateTimeField(auto_now_add = True) # 만들어진 날
    due_date = models.DateTimeField() # 언제까지 해야하는지
    done = models.BooleanField(default = False)# 했는지 안했는지

    def __str__(self):
        return self.todo
    