from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, login, \
    update_session_auth_hash
from django.contrib import messages  # Correct import for messages

from boekenclub.forms import ProfileForm, UserForm, BookForm
from boekenclub.models import Profile, Read, Book


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
def book_create(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        book_form.instance.submitted_by = request.user

        if book_form.is_valid():
            book = book_form.save(commit=False)

            if 'force' in request.POST and request.POST['force'] == '1' and request.user.is_superuser:
                book.approved = True
                book.approved_by = request.user

            book.save()

            messages.success(request, "Book created successfully and pending approval!" if not book.approved else "Book created successfully!")
            return redirect('book_list')
        else:
            messages.error(request, "An error occurred while creating the book. Please check the form.")
    else:
        book_form = BookForm()

    return render(request, "book/create.html", {'form': book_form, 'edit': False})


def books_list(request):
    if request.method == "POST":
        messages.error(request, "Invalid request method.")
        return redirect('books_list')

    books = Book.objects.all()

    ctx = {
        "public": books.filter(approved=True),
        "pending": books.filter(approved=False),
        "private": books.filter(submitted_by=request.user) if request.user.is_authenticated else [],
    }

    return render(request, "book/list.html", {'books': ctx})

@staff_member_required
def books_review(request):
    if request.method == "POST":
        messages.error(request, "Invalid request method.")
        return redirect('books_review')

    books = Book.objects.all()

    return render(request, "book/review.html", {'books': books.filter(approved=False)})

@staff_member_required
def book_accept(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.approved = True
    book.approved_by = request.user
    book.save()

    messages.success(request, f"Book '{book.title}' has been approved!")
    return redirect('books_review')

@staff_member_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    messages.success(request, f"Book '{book.title}' has been deleted!")
    return redirect('book_list')

@staff_member_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)

        if book_form.is_valid():
            book_form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_list')
        else:
            messages.error(request, "An error occurred while updating the book. Please check the form.")
    else:
        book_form = BookForm(instance=book)

    return render(request, "book/create.html", {'form': book_form, 'edit': True})


def book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if not book.approved and (not request.user.is_authenticated or (book.submitted_by != request.user and not request.user.is_superuser)):
        messages.error(request, "This book is not available for viewing.")
        return redirect('home')

    reads = Read.objects.filter(book=book).order_by('-date')
    average_score = reads.aggregate(models.Avg('score'))['score__avg'] or 0
    rated = Read.objects.filter(book=book, user=request.user).exists() if request.user.is_authenticated else False
    return render(request, "book/details.html",
                  {'book': book, 'reads': reads, 'average_score': average_score, 'rated': rated})


@login_required
def book_rate(request, pk, rating):
    print({'pk': pk, 'rating': rating})
    book = get_object_or_404(Book, pk=pk)

    if rating not in range(1, 6):
        messages.error(request, "Invalid rating. Please choose a value between 1 and 5.")
        return redirect('book_view', pk=pk)

    read, created = Read.objects.get_or_create(book=book, user=request.user, score=rating)
    read.score = rating
    read.save()

    messages.success(request, f"You rated '{book.title}' with a score of {rating}!")
    return redirect('book_view', pk=pk)

@login_required
def book_unrate(request, pk):
    book = get_object_or_404(Book, pk=pk)

    try:
        read = Read.objects.get(book=book, user=request.user)
        read.delete()
        messages.success(request, f"You have removed your rating for '{book.title}'.")
    except Read.DoesNotExist:
        messages.error(request, "You haven't rated this book yet.")

    return redirect('book_view', pk=pk)

@staff_member_required
def rating_delete(request, pk):
    read = get_object_or_404(Read, pk=pk)
    book = read.book
    user = read.user
    read.delete()
    messages.success(request, f"You have removed {user.username}'s rating for '{book.title}'.")
    return redirect('book_view', pk=book.pk)
