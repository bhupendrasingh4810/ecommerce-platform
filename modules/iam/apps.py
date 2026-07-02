from django.apps import AppConfig


class IAMConfig(AppConfig):
    """
    Configuration for the Identity and Access Management module.
    """

    default_auto_field = "django.db.models.BigAutoField"

    name = "modules.iam"

    label = "iam"

    verbose_name = "Identity and Access Management"

    def ready(self):
        """
        Code that should run when Django starts.

        We'll register signals here later.
        """
        pass
        # import modules.iam.signals 
        # later when we have signals to register