from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    items = Product.objects.all()
    
    context  = {'items':items, 'user':request.user}
    
    return render(request, 'base/home.html', context)


def viewShoe(request, pk):
    shoe = Product.objects.get(id=pk)
    shoe_comments = shoe.message_set.all()
    shoe_participants = shoe.participants.all()

    if request.method == 'POST':
        comment = Message.objects.create(
            user = request.user,
            shoe = shoe,
            body = request.POST.get("body")
        )
        shoe.participants.add(request.user)
        return redirect('shoe', pk=shoe.id)

    context = {'shoe':shoe, 'shoe_comments':shoe_comments}

    return render(request, 'base/shoe.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    
    return render(request, 'base/login_register.html', {'form':form})

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')
