from django.shortcuts import render, redirect
from django.contrib import auth
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User
from users.forms import LoginForm, SingUpForm

# Create your views here.

def singup(request):
    messages.get_messages(request).used = True
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['email']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
        
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = name
                user.save()
        
            except IntegrityError:
                messages.error(request, 'Email já em uso!')
                return redirect('singup')
        
            auth.login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('index')
        
        messages.error(request, 'Credenciais inválidas!')
        return redirect('singup')

    elif request.method == 'GET':
        form = SingUpForm()
        return render(request, 'users/singup.html', {'form': form})

def login(request):
    messages.get_messages(request).used = True
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
        
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login efetuado com sucesso!')
                return redirect('index')
            
            messages.error(request, 'Credenciais inválidas!')
            return redirect('login')
        
        messages.error(request, 'Credenciais inválidas!')
        return redirect('login')
    
    elif request.method == 'GET':
        return render(request, 'users/login.html', {'form': form})
    
def logout(request):
    messages.get_messages(request).used = True
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
