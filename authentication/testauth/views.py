from django.shortcuts import render, redirect

from . forms import CreateUserForm

def homepage(request):
    
    return render(request, 'testauth/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('my-login')
        
    context = {'registerform':form}


    return render(request, 'testauth/register.html', context=context)

def my_login(request):

    return render(request, 'testauth/mylogin.html')

def dashboard(request):

    return render(request, 'testauth/dashboard.html')

def about(request):

    return render(request, 'testauth/About.html')
