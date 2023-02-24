from .services.file_utils import *


class FormProcessor:

    @staticmethod
    def profile_data_form_process(request, jobseeker, form):
        cv_file = request.FILES.get('cv_file', False)
        if cv_file and validate_file_extension(str(cv_file)):
            save_form_data_in_db(cv_file, jobseeker, form)
        return cv_file


def save_form_data_in_db(cv_file, jobseeker, profile_data_form):
    new_data = profile_data_form.save(commit=False)
    new_data.cv_file = cv_file
    new_data.jobseeker = jobseeker
