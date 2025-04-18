from django.shortcuts import render
import random

# Create your views here.

def input(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        company = request.POST.get('company')
        gross_salary = float(request.POST.get('gross_salary', 0))
        tax = float(request.POST.get('tax', 0))
        bonus = float(request.POST.get('bonus', 0))

        # Compute net salary
        #net_salary = gross_salary - tax + bonus
        net_salary = gross_salary - (gross_salary * tax / 100) + (gross_salary * bonus / 100)

        # Create context for the result page
        context = {
            'name': name,
            'age': age,
            'company': company,
            'gross_salary': gross_salary,
            'tax': tax,
            'bonus': bonus,
            'net_salary': net_salary
        }

        return render(request, 'employeeapp/result.html', context)
    
    return render(request, 'employeeapp/salary_form.html')

def result(request):
    return render(request, 'employeeapp/result.html')
def jumble_words(request):
    context = {}
    if request.method == 'POST':
        word = request.POST.get('word', 'unknown')
        temp = list(word)
        random.shuffle(temp)
        word = ''.join(temp)
        context = {
            'word': word
        }
    return render(request, 'employeeapp/jumble_words.html', context)



