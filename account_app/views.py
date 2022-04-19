from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            newUser = form.save(commit=False)
            newUser.set_password(form.cleaned_data['password'])
            newUser.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account_app/register.html', context)
