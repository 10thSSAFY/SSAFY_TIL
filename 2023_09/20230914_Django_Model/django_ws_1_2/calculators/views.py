from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculators.html')


def result(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    mul = int(num1) * int(num2)
    sub = int(num1) - int(num2)
    if num2 != '0':
        divv = int(num1)/int(num2)
    else:
        divv = 'False'

    context = {
        'num1': num1,
        'num2': num2,
        'mul' : mul,
        'sub': sub,
        'divv': divv,
    }
    return render(request, 'calculators/result.html', context)