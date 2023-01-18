from .models import JobseekerRegisterInfo


class WithoutPasswordBackend:

    def authenticate(self, request, email=None, password=None):
        try:
            jobseeker = JobseekerRegisterInfo.objects.get(email=email)
            if jobseeker.check_password(password):
                return jobseeker
            return None
        except Exception:
            return None

    def get_user(self, user_id):
        try:
            return JobseekerRegisterInfo.objects.get(pk=user_id)
        except Exception:
            return None