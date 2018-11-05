# from django.apps import AppConfig
#
#
# class CustomersConfig(AppConfig):
#     name = 'customers'


from django.apps import AppConfig
from material.frontend.apps import ModuleMixin
from django.utils.translation import ugettext_lazy as _


class CustomersAppConfig(ModuleMixin, AppConfig):
    name = 'Customers'
    icon = '<i class="material-icons">extension</i>'
    verbose_name = _("Customers")

    def has_perm(self, user):
        return user.is_superuser