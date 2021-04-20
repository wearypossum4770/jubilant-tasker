from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

# def update_user(request, user_id):
def signout(request):
    logout(request)
    return redirect("/")


def check_authentication():
    pass


def index(request):
    return render(request, "index.html", {})


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, "homepage.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            form = AuthenticationForm(request.POST)
            return render(request, "signin.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "signin.html", {"form": form})


def update_profile(request):
    # users = User.objects.all().select_related('profile')
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _("Your profile was successfully updated!"))
            return redirect("settings:profile")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(
        request,
        "profiles/profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
