from resume.models import SocialAccount, Configuration


class GlobalContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["configurations"] = Configuration.objects.first()
        context["social_accounts"] = SocialAccount.objects.first()

        return context
