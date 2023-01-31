from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    result = 0
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operator = request.POST.get('operator')
        if len(number1) == 0 or len(number2) == 0:
            messages.error(request, 'Please enter the valid values')
        elif operator == '+':
            result = int(number1) + int(number2)
        elif operator == '-':
            result = int(number1) - int(number2)
        elif operator == '*':
            result = int(number1) * int(number2)
        elif operator == '/':
            result = int(number1) / int(number2)
        elif operator == '%':
            result = int(number1) % int(number2)

    return render(request, 'calculator_app/index.html',{'result':result})