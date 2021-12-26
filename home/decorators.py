from django.http import HttpResponse

def allowed_users(allowed_roles=[]):
    def decorator(veiw_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name 

            if group in allowed_roles:

                return veiw_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator