from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    # if request is POST, then a UserRegistrationForm() is instantiated
    # with the requests POST data passed as an argument
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to login.')
            return redirect('login')
    # else instantiate a blank UserRegistrationForm()
    else:
        form = UserRegistrationForm()
    # return register.html with form data as a context variable
    return render(request, 'users/register.html', {'form': form})

# decorators add functionality to an existing function


@login_required
def profile(request):
    if request.method == 'POST':
        # populating the form with the users current information
        # using instance=request.user and instance=request.user.profile
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated!')
            # by using redirect rather than letting the block reach
            # the render function this uses POST GET REDIRECT pattern
            # avoiding the "are you sure you want to resubmit this form"
            # message
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
