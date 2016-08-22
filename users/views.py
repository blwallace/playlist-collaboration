from django.shortcuts import render
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from .forms import UserCreateForm

def user_add(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
    else:
        form = UserCreateForm
        return render(request, 'users/form.html', {'form': form})

