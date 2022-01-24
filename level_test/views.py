from django.shortcuts import render

# Create your views here.
def level_test(request):
    
    return render(request, 'level_test/level_test.html')