#  _____      _                         _      _____ _____
# /  ___|    | |                       | |    |_   _|_   _|
# \ `--.  ___| |__  _ __ ___   ___  ___| | __   | |   | |
#  `--. \/ __| '_ \| '__/ _ \ / _ \/ __| |/ /   | |   | |
# /\__/ / (__| | | | | | (_) |  __/ (__|   <   _| |_  | |
# \____/ \___|_| |_|_|  \___/ \___|\___|_|\_\  \___/  \_/
import json

from django.shortcuts import render

from django_oauth_client.oauth import protected


@protected()
def home(request):
    user = json.loads(request.COOKIES.get('user'))
    return render(request, 'home.html', context={'user': user,
                                                 'user_name': user.get('name')})