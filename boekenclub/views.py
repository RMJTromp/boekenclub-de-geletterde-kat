from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, login, \
    update_session_auth_hash
from django.contrib import messages  # Correct import for messages
from urllib3 import request

from boekenclub.forms import ProfileForm, UserForm
from boekenclub.models import Profile, Read


@login_required
def home(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")

        return redirect('login')

    return render(request, "login.html")


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required
def profile_view(request, username):
    if request.user.username == username or request.user.is_staff:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            messages.error(request, "Profile not found.")
            return redirect('home')
    else:
        profile = Profile.objects.get(user=request.user)

    actions = Read.objects.filter(user=profile.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile', username=profile.user.username)
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'actions': actions,
        'profile': profile,
    }
    return render(request, "profile.html", context)


@login_required
def reset_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile', username=request.user.username)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }

    return render(request, "reset_password.html", context)


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()

            login(request, new_user)
            messages.success(request, "Your account has been created successfully!")
            return redirect('profile', username=new_user.username)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, "register.html", context)


@staff_member_required
def manage_users_view(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, "manage_users.html", context)


@staff_member_required
def delete_profile_view(request, user_id):
    if request.method != 'POST':
        messages.error(request, "Invalid request method.")
        return redirect('manage_users')

    try:
        user = get_object_or_404(User, id=user_id)
        username = user.username
        user.delete()
        messages.success(request, f"User '{username}' has been deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting user: {str(e)}")

    return redirect('manage_users')


@login_required
def delete_read_view(request, read_id):
    if request.method != 'POST':
        messages.error(request, "Invalid request method.")
        return redirect('profile', username=request.user.username)
    try:
        read = get_object_or_404(Read, id=read_id)
        title = read.book.title
        read.delete()
        messages.success(request, f"'{title}' has been deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting read: {str(e)}")

    return redirect('profile', username=request.user.username)