from django.shortcuts import render
from datetime import datetime
from .models import User
import random

QUOTES = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. – Nelson Mandela",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. – Martin Luther King Jr.",
]

def home(request):
    # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # return render(request, 'home.html', {'current_time': current_time})
    quote = random.choice(QUOTES)  # Select a random quote
    return render(request, 'home.html', {'quote': quote})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        user = User(name=name, email=email , phone=phone, gender=gender)
        user.save()
        context={
            'name': name,
            'email': email,
            'phone': phone,
            'gender': gender
        }
        return render(request, 'form_success.html', context)
    return render(request, 'home.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

