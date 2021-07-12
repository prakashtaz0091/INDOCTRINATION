from django.shortcuts import render,redirect
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile,User
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
                


               # messages.success(request,f"Account successfully created for {username}")
                request.session['username'] = username
              
                return redirect('createProfile')


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
    name = request.user.profile.name

    username = request.user.username
    address = request.user.profile.address
    phone_no = request.user.profile.phoneNo
    level = request.user.profile.level
    disability = request.user.profile.disability
    context ={
        'userinfo':True,
        'name':name,
        'username':username,
        'address':address,
        'phone_no':phone_no,
        'level':level,
        'disability':disability,
    }
    return render(request,'profile.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')



def createProfile(request):   # creating profile after the registration done
    
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = request.session['username']
            user = User.objects.get(username=username)
            user = user
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            phoneNo = form.cleaned_data.get('phoneNo')
            dob = form.cleaned_data.get('dob')
            level = form.cleaned_data.get('level')
            disabled = form.cleaned_data.get('disabled')

            Profile.objects.create(
                user = user,
                name = name,
                address = address,
                phoneNo = phoneNo,
                dob = dob,
                level = level,
                disability = disabled,

            )
           
            messages.success(request,f"Account successfully created for {username}")
            return redirect('loginPage')


    profileForm = ProfileForm()

    context = { 
        'profileForm':profileForm,
    }

    return render(request,'createProfile.html',context)
