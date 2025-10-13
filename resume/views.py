from django.views.generic.list import ListView
from resume.models import (
    Jumbotron,
    TechSkill,
    Job,
    Education,
    Language,
    SocialAccount,
    Configuration,
    Menu,
    SubMenu,
)


class ResumeView(ListView):
    
    queryset = Configuration.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jumbotron"] = Jumbotron.objects.first()
        context["tech_skills"] = TechSkill.objects.first()
        context["jobs"] = Job.objects.all()
        context["educations"] = Education.objects.all()
        context["languages"] = Language.objects.all()
        context["social_accounts"] = SocialAccount.objects.first()
        context["configurations"] = Configuration.objects.all()
        context["parent_menu"] = Menu.objects.filter(icon_type="DD")
        context["single_menu"] = Menu.objects.filter(icon_type="N")
        context["disabled_menu"] = Menu.objects.filter(icon_type="DI")
        context["submenu"] = SubMenu.objects.all()
        return context