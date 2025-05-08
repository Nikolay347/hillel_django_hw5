from django.contrib.auth.mixins import UserPassesTestMixin
from first_app.utils import is_user_superuser


class UserIsAdminMixin(UserPassesTestMixin):

    def test_func(self):
        return is_user_superuser(self.request.user)