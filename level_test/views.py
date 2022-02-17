from django.shortcuts import render
from .models import Question


def level_test(request):
   
    question_counter = 1
    question = Question.objects.get(question_number=question_counter)
    total = 0
    
    context = {
        'question': question,
        'question_counter':question_counter,
        'total':total,
    }
    return render(request, 'level_test/level_test.html', context)

    
def check_answer(request, question_counter, total):
    
    total_qs = Question.objects.all().count()
    current_question = Question.objects.get(question_number=question_counter)
    correct_answer = current_question.correct_answer
    result_key={
        range(0,4):'A1 - Beginner',
        range(4,7):'A2 - Elementary',
        range(7,10):'B1 - Pre-Intermediate',
        range(10,14):'B2 - Intermediate',
        range(14,17):'B2H - Upper Intermediate',
        range(17,20):'C1 - Advanced'
        }
       
    # Finish test after last question and return result page
    if question_counter == total_qs:
        
        question= Question.objects.get(question_number=question_counter)
        answer = request.GET['answer']
        
        if answer == correct_answer:
            result=''
            total +=1
            for key in result_key:
                if total in key:
                    result = result_key[key]
                    break
             
            context={
                'total':total,
                'result':result,
            }
            return render(request, 'level_test/level_test_results.html', context)
        else:
            for key in result_key:
                if total in key:
                    result = result_key[key]
                    break
            context={
                'total':total,
                'result':result
            }
            return render(request, 'level_test/level_test_results.html', context)
    
    else:
        question_counter += 1
        question= Question.objects.get(question_number=question_counter)
        answer = request.GET['answer']
        if answer == correct_answer:
            total +=1
        
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

