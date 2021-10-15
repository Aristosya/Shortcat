from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usename = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.warning(request,
                             f'Пользователь {usename} успешно зарегистрирован.\nНе забудь проверить почтовый ящик {email} и подтвердить регистрацию.(Пока не работает)')
            return redirect('main')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)


        if profileForm.is_valid() or updateUserForm.is_valid():
            if profileForm.is_valid():
                profileForm.save()
            if updateUserForm.is_valid():
                updateUserForm.save()
            messages.warning(request,
                             f'Изменения примененны')
            return redirect('profile')

    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
    }
    return render(request, 'registration/profile.html', data)
