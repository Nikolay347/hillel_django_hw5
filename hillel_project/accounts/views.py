from django.contrib.auth.views import (
    LoginView as BaseLoginView
)
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme


class LoginView(BaseLoginView):

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={self.request.get_host()},
                require_https=self.request.is_secure(),
        ):
            return next_url

        return reverse_lazy("home")


