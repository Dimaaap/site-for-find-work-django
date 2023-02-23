import logging

from django.shortcuts import redirect

logger = logging.getLogger('jobseeker')


def redirect_login_user(view_func, redirect_url='index_page'):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_url, permanent=True)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper
