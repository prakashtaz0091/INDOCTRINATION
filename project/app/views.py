from django.shortcuts import render,redirect
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile,User
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from asgiref.sync import sync_to_async,async_to_sync
import os
import asyncio 

# from pynput import keyboard






# google text to speech module
from gtts import gTTS


def welcome(name):  # for welcome speech
    # print('inside welcome')
    text = f" Indoctrination maa hajurlai swagat chha, {name}!.  Ma hajurlai k sahayog garna sakchhu ?"
    voice = gTTS(text=text, lang='hi',slow=False)
    voice.save("welcome.mp3")  # saves voice as welcome.mp3
    os.system("mpg321 welcome.mp3")  # plays that mp3 file
    voice.stop()
     

@sync_to_async  #since request.user is synchronous only
def is_blind(request):
    if request.user.profile.disability == "blind":
        return True
    else:
        return False




@sync_to_async
def is_first_time(request): # converts sync to async , since request.session cannot be made async
    return request.session['first_time_entry']

@sync_to_async # since request.user.profile.name cannot be converted to async
def get_name(request):
    return request.user.profile.name


"""
def listenChoice(request):
    def on_press(key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
            print(k)
            if(k == '1'):
                print('pressed 1')
                
                return 'profile.html'
        

        except:
            k = key.name  # other keys
        if k in ['space']:  # keys of interest
            # self.keys.append(k)  # store it in global-like variable
            print('Key pressed: ' + k)
            return False  # stop listener; remove this if want more keys
    

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys

    return on_press
"""
@sync_to_async
def blindnav():
    text = "please enter 1, to go to home. enter 2, to go to course section. enter 3, to go to blog section. enter 4, to go to live tutor. enter 5, to know more about us. enter 6, to go to contact us"
    voice = gTTS(text=text, lang='hi',slow=False)
    voice.save("blindnav.mp3")  # saves voice as welcome.mp3
    os.system("mpg321 blindnav.mp3")  # plays that mp3 file
    voice.stop()


@sync_to_async
@login_required(login_url='loginPage')
@async_to_sync
async def home(request):
    

    name = await get_name(request)
    first_time_entry = await is_first_time(request) #identifying that the use has entered home page first time after login, this session is created in login view
  
    if first_time_entry:
        a_welcome = sync_to_async(welcome)
        task1 = asyncio.create_task(a_welcome(name))
        request.session['first_time_entry'] = False             # after first time welcome speech, setting first time entry session to false, so that welcome speech don't run again and again

    blind = await is_blind(request)
    print(blind)
    if blind:
        asyncio.create_task(blindnav())

    # a_listenChoice = sync_to_async(listenChoice)
    # task = asyncio.create_task(a_listenChoice(request))
    
    context = {
        'name':name,
        'blind':blind,
    }
    # await task1
    a_render = sync_to_async(render) #converting render method to async then calling it as coroutine
    return await a_render(request,'home.html',context)





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


@unauthenticated_user    # if unauthenticated then send user login page
def loginPage(request):
    
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                request.session['first_time_entry']=True
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



def courses(request):
    return render(request,'courses.html')



def course2(request):
    return render(request,'course2.html')


def course3(request):
    return render(request,'course3.html')


def subject_detail(request):

    
    return render(request,'subject.html')



def live_tutors(request):
    return render(request,'live_video.html')


