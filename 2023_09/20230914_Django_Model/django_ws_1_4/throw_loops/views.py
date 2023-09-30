import random
from django.shortcuts import render

# Create your views here.
def first(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'throw_loops/first.html', context)


def second(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'throw_loops/second.html', context)


def third(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    message = random.choice([message1, message2])
    context = {
        'message': message,
    }
    return render(request, 'throw_loops/third.html', context)