from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Outputs empty form registration
        form = UserCreationForm()

    else:
        # Processing the completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in and redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Output empty form or invalid page
    context = {'form': form}
    return render(request, 'users/register.html', context)

def logout_confirm(request):
    return render(request, 'users/logout_confirm.html')

