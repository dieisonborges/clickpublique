from django.shortcuts import render
from .models import StoreWoo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/usuarios/login/')
def list_stores(request):
    #print("OK ****************8")
    template_name = 'list_stores.html'
    context = {}
    #stores = {}    
    stores = StoreWoo.objects.filter(user=request.user)
    print("******************************")
    print(stores)
    print("******************************")
    context['stores'] = stores
    
    
    return render(request, template_name, context)

'''
def add_woocomerce(request):
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
'''
