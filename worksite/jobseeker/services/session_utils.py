from jobseeker.models import JobseekerRegisterInfo


def unpack_session_tuple_in_user(session_tuple: tuple) -> JobseekerRegisterInfo:
    user = JobseekerRegisterInfo(full_name=session_tuple[0], phone_number=session_tuple[1], email=session_tuple[2],
                                 password=session_tuple[3])
    return user


def write_session_args_as_tuple(request, *args):
    request.session['session_tuple'] = args
    print(request.session['session_tuple'])
