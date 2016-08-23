from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .forms import UserCreateForm, UserLoginForm

def user_add(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserCreateForm
        return render(request, 'users/form.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})


def user_authenticate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # If user is authenticated and active, login and navigate to success page
        if user is not None and user.is_active:
            login(request, user)
            return redirect('user_detail', pk=user.pk)
        else:
            form = UserLoginForm
            form.message = "Login Error"
            return render(request, 'users/form.html', {'form': form})
    # Else return the login page
    form = UserLoginForm
    return render(request, 'users/form.html', {'form': form})


def user_logout(request):
    logout(request)
    form = UserLoginForm
    return render(request, 'users/form.html', {'form': form})

