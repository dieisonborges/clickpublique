from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm, UserProfileForm, UserFormChangeInformation
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect

def add_user_register(request):
    template_name = 'add_user_register.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Criado com sucesso!')
            return HttpResponseRedirect('/')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)

def user_login(request):
    template_name = 'user_login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect(request.GET.get('next', '/'))
            #return HttpResponseRedirect(request.POST.get('next'))
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return render(request, template_name, {})

@login_required(login_url='/usuarios/login/')
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

@login_required(login_url='/usuarios/login/')
def user_change_password(request):
    template_name = 'user_change_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():            
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Senha modificada com sucesso!')
        else:
            messages.error(request, 'Não foi possível modificar sua senha')
    form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def add_user_profile(request):    
    template_name = 'add_user_profile.html'
    context = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                messages.success(request, 'Modificado com sucesso!')
        except MultipleObjectsReturned:
            messages.error(request, 'Já existe um perfil!')
    form = UserProfileForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def list_user_profile(request):
    template_name = 'list_user_profile.html'
    return render(request, template_name, {})

@login_required(login_url='/usuarios/login/')
def change_user_profile(request, username):
    template_name = 'add_user_profile.html'
    context = {}
    profile = UserProfile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado com sucesso!')
    form = UserProfileForm(instance=profile)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/usuarios/login/')
def change_user_information(request, username):
    template_name = 'change_user_information.html'
    context = {}
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UserFormChangeInformation(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado com sucesso!')
    form = UserFormChangeInformation(instance=user)
    context['form'] = form
    return render(request, template_name, context)
