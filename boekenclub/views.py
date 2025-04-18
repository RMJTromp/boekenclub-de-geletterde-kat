from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from boekenclub.forms import ProfileForm
from boekenclub.models import Profile, Read


@login_required
def home(request):

    return render(request, "index.html")

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            error_message = "Please enter both username and password."
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                error_message = "Invalid username or password."

        return render(request, "login.html", {"error_message": error_message})

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
            return redirect('home')
    else:
        profile = Profile.objects.get(user=request.user)

    actions = Read.objects.filter(user=profile.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=profile.user.username)
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'actions': actions
    }
    return render(request, "profile.html", context)


def reset_password_view(request):
    return None


def register(request):
    return None


def manage_users_view(request):
    return None