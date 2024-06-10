import json

import requests
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import redirect, render

from .forms import MemoryForm
from .models import Memory


def home(request):
    if request.user.is_authenticated:
        memories = Memory.objects.filter(user=request.user)
        memories_json = json.dumps(list(memories.values()), cls=DjangoJSONEncoder)
        avatar_url = request.session.get("avatar_url")

        context = {
            "memories": memories,
            "memories_json": memories_json,
            "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
            "avatar_url": avatar_url,
        }

        return render(request, "memories/home.html", context)
    else:
        return render(request, "memories/welcome.html")


def login_view(request):
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?response_type=code"
        "&client_id={client_id}"
        "&redirect_uri={redirect_uri}"
        "&scope=openid%20email%20profile"
        "&access_type=offline"
        "&prompt=select_account"
    ).format(
        client_id=settings.GOOGLE_CLIENT_ID,
        redirect_uri=settings.GOOGLE_REDIRECT_URI,
    )
    return redirect(google_auth_url)


def oauth2callback(request):
    code = request.GET.get("code")
    if not code:
        return redirect("home")

    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_r = requests.post(token_url, data=token_data)
    token_json = token_r.json()

    access_token = token_json.get("access_token")

    user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    user_info_params = {"access_token": access_token}
    user_info_r = requests.get(user_info_url, params=user_info_params)
    user_info = user_info_r.json()

    user, created = User.objects.get_or_create(
        username=user_info["name"],
        defaults={
            "first_name": user_info["given_name"],
            "last_name": user_info["family_name"],
            "email": user_info["email"],
        },
    )

    login(request, user)
    request.session["avatar_url"] = user_info.get("picture")

    return redirect("home")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def add_memory(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.latitude = round(memory.latitude, 6)
            memory.longitude = round(memory.longitude, 6)
            memory.save()
            return redirect("home")
        else:
            print("Error:", form.errors)
    else:
        form = MemoryForm()

    context = {
        "form": form,
        "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
    }

    return render(request, "memories/add_memory.html", context)
