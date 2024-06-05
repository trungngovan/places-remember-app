from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Memory
import json
from django.core.serializers.json import DjangoJSONEncoder


def home(request):
    if request.user.is_authenticated:
        memories = Memory.objects.filter(user=request.user)
        memories_json = json.dumps(list(memories.values()), cls=DjangoJSONEncoder)
        social_account = request.user.socialaccount_set.first()
        avatar_url = social_account.get_avatar_url() if social_account else None

        context = {
            'memories': memories,
            'memories_json': memories_json,
            'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
            'avatar_url': avatar_url
        }

        return render(request, 'memories/home.html', context)
    else:
        return render(request, 'memories/welcome.html')


@login_required
def add_memory(request):
    if request.method == 'POST':
        place_name = request.POST['place_name']
        comments = request.POST['comments']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        Memory.objects.create(user=request.user, place_name=place_name, comments=comments, latitude=latitude,
                              longitude=longitude)
        return redirect('home')
    return render(request, 'memories/add_memory.html', {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})
