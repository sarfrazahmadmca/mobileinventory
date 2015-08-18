from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .decorators import sales_person_required


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class OnlySalesPersonRequiredMixin(object):
    @method_decorator(sales_person_required)
    def dispatch(self, *args, **kwargs):
        return super(OnlySalesPersonRequiredMixin, self).dispatch(*args, **kwargs)
