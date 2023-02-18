from datetime import datetime, timedelta

from django.conf import settings


class TimeAccessMiddleware:

    def __init__(self, get_response: callable):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        current_datetime = datetime.now()
        string_strptime = datetime.strptime(request.session['last_access'], settings.DATE_FORMAT)
        if (request.session.get('last_access') is None
                or self.comparing_two_dates(second_time=string_strptime)):
            request.session['access'] = True
            request.session['last_access'] = str(current_datetime)
            response = self.get_response(request, *args, **kwargs)  # view
            return response
        else:
            request.session['access'] = False
            raise AttributeError('Time access')

    @staticmethod
    def comparing_two_dates(second_time: datetime, period: int | float = 12,
                            first_time: datetime = datetime.now()):
        return first_time >= second_time + timedelta(seconds=3)
