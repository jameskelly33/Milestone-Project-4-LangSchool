from django.shortcuts import render
from .models import Question

# Create your views here.
def level_test(request):
   
    question_counter = 1
    question = Question.objects.get(question_number=question_counter)
    total = 0
    
    context = {
        'question': question,
        'question_counter':question_counter,
        'total':total
    }
    return render(request, 'level_test/level_test.html', context)

    
def check_answer(request, question_counter, total):
    
    total_qs = Question.objects.all().count()
    current_question = Question.objects.get(question_number=question_counter)
    correct_answer = current_question.correct_answer
    if question_counter == total_qs:
        
        question= Question.objects.get(question_number=question_counter)
        answer = request.GET['answer']
        if answer == correct_answer:
            total +=10
            context={
                'total':total,
            }
            return render(request, 'level_test/level_test_results.html', context)
        else:

            context={
                'total':total,
            }
            return render(request, 'level_test/level_test_results.html', context)
       
    else:
        question_counter += 1
        question= Question.objects.get(question_number=question_counter)
        answer = request.GET['answer']
        if answer == correct_answer:
            total +=10
        
            
        
        context = {
                'question':question,
                'current_question':current_question,
                'correct_answer':correct_answer,
                'answer': answer,
                'question_counter':question_counter,
                'total':total,
                'total_qs':total_qs
            }
        return render(request, 'level_test/level_test.html', context)

