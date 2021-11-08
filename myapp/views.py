from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

def home(request):
    context = {}
    context['hello'] = _('Hello')
    output = _(str(request.user))
    print(output)
    context['user'] = output
    if not request.user.is_anonymous:
        context['user'] = output
        print(context['user'])
        if request.user.is_superuser:
            return redirect('admin/')
        else:
            return render(request, 'index.html', context)
    else:
        output = _('Register or Login ?')
        context['user'] = output
        print(context['user'])
        return render(request, 'index.html', context)

'''def translate(language, text):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext(text)
    finally:
        activate(cur_language)
    print(text)
    return text'''
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