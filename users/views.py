from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from .forms import UserCreateForm

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