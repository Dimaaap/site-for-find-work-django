from datetime import datetime, timedelta, date

from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages


def limiter_time_view(view_func: callable, redirect_url='jobseeker_profile'):
    def wrapper(request, *args, **kwargs):
        last_visit_time = request.session.get('last_visit_time')
        current_time = datetime.now()
        if last_visit_time:
            last_visit_time = datetime.strptime(last_visit_time, settings.DATE_FORMAT)
            time_delta = current_time - last_visit_time
            if time_delta.total_seconds() < settings.SIX_HOURS_IN_SECONDS:
                time_left = str(timedelta(seconds=settings.SIX_HOURS_IN_SECONDS -
                                          time_delta.total_seconds()))
                messages.error(request, f"Змінювати пароль можна один раз на "
                                        f"6 годин. Повторіть спробу через {str(time_left)[:1]} "
                                        f"годин та {time_left[2:4]} хвилин")
                request.session['time_left'] = str(datetime.strptime(time_left, settings.TIME_FORMAT))
                request.session['view_access'] = False
                return redirect(redirect_url, request.session['login'])
        response = view_func(request, *args, **kwargs)
        request.session['view_access'] = True
        request.session['last_visit_time'] = str(current_time)
        return response

    return wrapper
