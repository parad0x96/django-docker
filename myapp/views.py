from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):
    context = {}
    if not request.user.is_anonymous:
        context['user'] =str(request.user)
        print(request.user.is_superuser)
        if request.user.is_superuser:
            print('wtf ??')
            return redirect('admin/')
        else:
            return render(request, 'index.html', context)
    else:
        context['user'] = 'Register or Login ?'
        return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})