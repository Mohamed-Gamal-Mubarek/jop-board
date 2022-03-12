from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        pass
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
    return render(request, 'accounts/profile_edit.html', {'userForm':userForm})
