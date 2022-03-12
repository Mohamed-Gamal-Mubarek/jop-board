from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import SignupForm, UserForm , ProfileForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    # GET CURRENT USER LOGIN IN THE SYSTEM OR YOUR APPLICATION
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    # TO AVOID ERROR FOR CHEKING THE PAGE DON'T USE THE BUTTON AT FIRST REMMEMBER THAT
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = ProfileForm(request.POST, instance=profile) 
        if(userForm.is_valid() and profileForm.is_valid()):
            userForm.save()
            actionProfile = profileForm.save(commit=False)
            actionProfile.user = request.user
            actionProfile.save()
            return redirect(reverse('accounts:profile'))
            pass
    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=profile)
    
    context = {
        
        'userForm':userForm,
        'profileForm': profileForm
    }
    return render(request, 'accounts/profile_edit.html', context)
