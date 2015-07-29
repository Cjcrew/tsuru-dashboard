from django.views.generic import TemplateView

from auth.views import LoginRequiredMixin

import os


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'autoscale/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        token = self.request.session.get('tsuru_token').split(' ')[1]
        service_url = "{}?TSURU_TOKEN={}".format(os.environ.get("AUTOSCALE_DASHBOARD_URL"), token)
        context["service_url"] = service_url
        return context
