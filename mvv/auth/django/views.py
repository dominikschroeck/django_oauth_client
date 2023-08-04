#  _____      _                         _      _____ _____   _____                       _ _   _
# /  ___|    | |                       | |    |_   _|_   _| /  __ \                     | | | (_)
# \ `--.  ___| |__  _ __ ___   ___  ___| | __   | |   | |   | /  \/ ___  _ __  ___ _   _| | |_ _ _ __   __ _
#  `--. \/ __| '_ \| '__/ _ \ / _ \/ __| |/ /   | |   | |   | |    / _ \| '_ \/ __| | | | | __| | '_ \ / _` |
# /\__/ / (__| | | | | | (_) |  __/ (__|   <   _| |_  | |   | \__/\ (_) | | | \__ \ |_| | | |_| | | | | (_| |
# \____/ \___|_| |_|_|  \___/ \___|\___|_|\_\  \___/  \_/    \____/\___/|_| |_|___/\__,_|_|\__|_|_| |_|\__, |
#                                                                                                       __/ |
#                                                                                                      |___/

import json
from functools import wraps

from authlib.integrations.django_client import OAuth

from .settings import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


oauth = OAuth()
oauth.register(
    name='keycloak',
    server_metadata_url=settings.OAUTH_CONF_URL,
    # client_id="test-app-django",
    # client_secret="oPEK2!HpHqPdLCffMP9",
    client_kwargs={
        'scope': 'openid email profile'
    }
)


def protected(f):
    @wraps(f)
    def decorator(request, *args, **kwargs):
        if request.COOKIES.get('user'):
            return f(request, *args, **kwargs)
        else:
            return redirect('/login/')

    return decorator


def login(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.keycloak.authorize_redirect(request, redirect_uri)


def auth(request):
    token = oauth.keycloak.authorize_access_token(request)
    response = HttpResponseRedirect("/")
    response.set_cookie('user', json.dumps(token['userinfo']))
    return response


def logout(request):
    response = HttpResponseRedirect("/")
    response.delete_cookie('user')
    return response
