from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_number',
        'question_text',
        'option1',
        'option2',
        'option3',
        'option4',
        'correct_answer'
    )


admin.site.register(Question, QuestionAdmin)
