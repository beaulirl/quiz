from django.contrib import admin

# Register your models here.

from .models import Question, User, Answer, Test, TestQuestion, UserAnswer, Level

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(UserAnswer)
admin.site.register(Level)

