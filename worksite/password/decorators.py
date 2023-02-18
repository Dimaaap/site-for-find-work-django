import functools
from datetime import datetime, timedelta

from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages

from .services import comparing_two_dates


def limiter_access_in_time(view_function, redirect_url='jobseeker_profile'):
    @functools.wraps(view_function)
    def inner(request, *args, **kwargs):
        current_datetime = datetime.now()
        string_strptime = datetime.strptime(request.session['last_access'], settings.DATE_FORMAT)
        if (request.session.get('last_access') is None
                or comparing_two_dates(second_time=string_strptime)):
            request.session['access'] = True
            request.session['last_access'] = str(current_datetime)
            return view_function(request, *args, **kwargs)
        else:
            request.session['access'] = False
            messages.error(request, 'Змінювати пароль можна один раз кожні 12 годин')
            return redirect(redirect_url, request.session['login'])

    return inner
