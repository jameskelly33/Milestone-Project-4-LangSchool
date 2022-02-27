from django.db import models


class Question(models.Model):
    question_number = models.DecimalField(max_digits=2, decimal_places=0)
    question_text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)
