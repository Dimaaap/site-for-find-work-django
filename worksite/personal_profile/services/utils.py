from django.core.exceptions import ObjectDoesNotExist

from .check_cleaned_data import check_cleaned_data
from .db_utils import filter_fields_from_db, get_fields_from_db
from ..models import JobseekerProfileInfo, Country, City
from ..forms import ProfileInfoForm
from ..country_parser import DBSaver
from ..city_parser import DBSaver as CitySaver


def update_form_data(form: callable, model: callable, filter_args: tuple):

    fields = dict(form.cleaned_data).keys()
    list_fields = list(fields)
    check_cleaned_data(list_fields, form.cleaned_data)
    if len(filter_args) != 2:
        raise ValueError('filter_args arguments must have strictly 2 elements')
    else:
        filter_data = filter_fields_from_db(model, *filter_args)
        filter_data.update(**form.cleaned_data)


def update_cv_field_in_model(model: callable, tuple_args: tuple, cv_file: open):
    query = get_fields_from_db(model, *tuple_args)
    if cv_file:
        try:
            query.cv_file = cv_file
            query.save()
        except Exception:
            return False
    return True


def create_jobseeker_profile_service(jobseeker: callable, key: str, value):
    try:
        jobseeker_data = get_fields_from_db(JobseekerProfileInfo, key, value)

        jobseeker_profile = jobseeker_data
        return jobseeker_profile
    except ObjectDoesNotExist:
        jobseeker_profile = JobseekerProfileInfo(jobseeker=jobseeker)
        jobseeker_profile.save()
        print(jobseeker_profile)
        return jobseeker_profile


def set_field_initial_values(request, jobseeker_profile: JobseekerProfileInfo):
    if jobseeker_profile:
        initial_values = {'expected_job': jobseeker_profile.expected_job,
                          'telegram': jobseeker_profile.telegram,
                          'linkedin': jobseeker_profile.linkedin,
                          'git_hub': jobseeker_profile.git_hub}
        profile_data_form = ProfileInfoForm(request.POST or None, initial=initial_values)
    else:
        profile_data_form = ProfileInfoForm(request.POST or None)
    return profile_data_form


