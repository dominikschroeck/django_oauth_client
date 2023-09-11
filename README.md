# OAuth Login with Django

This README.md provides instructions on implementing OAuth login within your Django application. OAuth integration allows you to replace local authentication with a remote Identity Provider (IdP) while enabling role-based access control for specific endpoints.

## How to Secure Your Endpoints

Securing your endpoints using OAuth is a straightforward process:

1. **Configure Application Environment**: First, set up the necessary environment variables you received from your IdP administrator. Replace `<client-id>` and `<client-secret>` with the provided values. The `OAUTH_SCOPE` variable specifies the required access scopes, and `OAUTH_METADATA_URL` should point to your IdP's OpenID configuration.

    ```shell
    export OAUTH_CLIENT_ID="<client-id>"
    export OAUTH_CLIENT_SECRET="<client-secret>"
    export OAUTH_SCOPE="profile openid email"
    export OAUTH_METADATA_URL="http://127.0.0.1:8100/realms/master/.well-known/openid-configuration"
    ```


2. **Add OAuth Views to URLs**: In your Django `urls.py`, import and include the `login`, `auth`, and `logout` views provided by this package. These views are responsible for handling OAuth authentication.

    ```python
    from django.urls import path
    from mvv.auth.django.oauth import login, auth, logout

    urlpatterns = [
        ... # other URLs
        path('login/', login),
        path('auth', auth),
        path('logout/', logout),
    ]
    ```

    With these URL patterns, you'll have endpoints for initiating the OAuth login (`/login/`), handling authentication callbacks (`/auth`), and logging out (`/logout/`).


3. **Protect Endpoints with Roles**: To restrict access to specific endpoints based on roles, use the `@protected` decorator provided by this package in your `views.py` file. In this example, we protect the `protected_endpoint` view, allowing only users with the "admin" role to access it.

    ```python
    from mvv.auth.django.oauth import protected

    @protected(roles=["admin"])
    def protected_endpoint(request):
        """
        A protected endpoint that only users with the "admin" role can access.
        """

        return "OK"
    ```

    By applying the `@protected` decorator to your views, you can enforce role-based access control on your Django application's endpoints, ensuring that only authorized users can access protected resources.

4. ** How to retrieve a token for API Access**: Simply access the ``login`` endpoint with an additional ``?token=True`` from your browser once to get a token from Keycloak that you can use as ``Bearer`` token in the ``Authorization`` header.

By following these steps, you can seamlessly integrate OAuth authentication into your Django application, enhancing security and access control for your users.

Contact: [hello@schroeck-consulting.de](mailto:hello@schroeck-consulting.de)