from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Partial(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        template_name = kwargs['template_name']
        if template_name.endswith("/"):
            template_name = template_name[:-1]
        self.template_name = 'softworks/partials/%s.html' % (template_name)
        return super(Partial, self).dispatch(request, *args, **kwargs)


class PrivatePartial(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        template_name = kwargs['template_name']
        if template_name.endswith("/"):
            template_name = template_name[:-1]
        self.template_name = 'softworks/private_partials/%s.html'\
            % (template_name)
        return super(PrivatePartial, self).dispatch(request, *args, **kwargs)
