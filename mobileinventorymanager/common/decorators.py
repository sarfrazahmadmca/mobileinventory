from django.core.exceptions import PermissionDenied


def sales_person_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not hasattr(request.user, 'salesperson'):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view_func
