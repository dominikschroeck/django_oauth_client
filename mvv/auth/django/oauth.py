#  _____      _                         _      _____ _____
# /  ___|    | |                       | |    |_   _|_   _|
# \ `--.  ___| |__  _ __ ___   ___  ___| | __   | |   | |
#  `--. \/ __| '_ \| '__/ _ \ / _ \/ __| |/ /   | |   | |
# /\__/ / (__| | | | | | (_) |  __/ (__|   <   _| |_  | |
# \____/ \___|_| |_|_|  \___/ \___|\___|_|\_\  \___/  \_/

import json
import logging

from authlib.integrations.django_client import OAuth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from mvv.auth.common.settings import oauth_settings

logger = logging.getLogger(__name__)

oauth = OAuth()
oauth.register(
    name='keycloak',
    server_metadata_url=oauth_settings.oauth_metadata_url,
    client_id=oauth_settings.oauth_client_id,
    client_secret=oauth_settings.oauth_client_secret,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


def protected(roles: list = None):
    """
    Protect endpoints with role assignment (optional)
    """

    def inner(f):
        """
        Inner decorator to store 'roles' in this function object
        """

        def wrapper(request, *args, **kwargs):
            """

            """
            try:
                user = json.loads(
                    request.COOKIES.get('user')) if request.COOKIES.get(
                    'user') else None
            except:
                logger.warning("Unable to parse user cookie into dictionary!")
                return redirect("/login/")

            if user:
                if roles:
                    for role in roles:
                        if role in user.get('roles'):
                            return f(request, *args, **kwargs)
                        return HttpResponse('You are not allowed to '
                                            'access this page due to missing '
                                            'role assignment. Speak to your '
                                            'admin if you believe this is a '
                                            'mistake', status=401)
                return f(request, *args, **kwargs)

            return redirect('/login/')

        return wrapper

    return inner


def login(request):
    """

    :param request:
    :return:
    """
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.keycloak.authorize_redirect(request, redirect_uri)


def auth(request):
    """

    :param request:
    :return:
    """
    token = oauth.keycloak.authorize_access_token(request)

    response = HttpResponseRedirect("/")
    response.set_cookie('user', json.dumps(token['userinfo']))
    return response


def logout(request):
    """

    :param request:
    :return:
    """
    # response = HttpResponseRedirect("/")
    response = HttpResponse("You have been logged out!!"
                            '<a href="/">Back to home</a>')
    if request.COOKIES.get('user'):
        response.delete_cookie('user')
    return response
