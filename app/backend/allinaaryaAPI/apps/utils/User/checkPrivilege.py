import collections

from django.http import HttpResponse

from apps.utils.User.userUtility import getUserPrivileges

def has_privilege(allowed_privileges=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if (not allowed_privileges) or userHasPrivilege(allowed_privileges, getUserPrivileges(request.user.pk)):
                return view_func(request, *args, **kwargs)
            return HttpResponse('You are not authorised to view this page')
        return wrapper_func
    return decorator

def userHasPrivilege(allowed_privileges, userPrivileges):
    for allowed_privilege in allowed_privileges:
        if allowed_privilege.name not in userPrivileges:
            return False
    return True
