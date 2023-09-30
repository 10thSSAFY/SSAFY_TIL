from django.shortcuts import render

# Create your views here.
def converter(request, num1, num2):
    mul = num1 * num2
    sub = num1 - num2
    if num2 != 0:
        divv = num1 / num2
    else:
        divv = False

    context = {
        'num1': num1,
        'num2': num2,
        'mul': mul,
        'sub': sub,
        'divv': divv,
    }
    return render(request, 'calculators/calculator.html', context)