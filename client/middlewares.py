from django.shortcuts import redirect
from django.conf import settings


class ClientAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated \
                and not request.path.startswith('/register') \
                and not request.path.startswith('/password_reset') \
                and not request.path.startswith('/password_reset_confirm') \
                and not request.path.startswith('/login') \
                and not request.path.startswith('/jet') \
                and not request.path.startswith('/api')\
                and not request.path.startswith('/logout')\
                and not request.path.startswith('/admin'):
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # Code to be executed for each request/response after
        # the view is called.

        return response