from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user




@login_required(login_url='loginPage')
def home(request):
    return render(request, 'home.html')



@unauthenticated_user
def registerPage(request):
 
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')


                messages.success(request,f"Account successfully created for {username}")
                return redirect('loginPage')


        context = {
            'form':form,
        }
        return render(request,'registerPage.html',context)



@unauthenticated_user
def loginPage(request):
    
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request,'Username or Password is Incorrect ! Please try again')
                return redirect('loginPage')

        return render(request,'loginPage.html')



def profile(request):
    return render(request,'profile.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')