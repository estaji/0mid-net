from django.views.generic.list import ListView
from core.models import Menu, SubMenu
from resume.models import (
    Configuration,
    SocialAccount,
    Jumbotron,
    Job,
    Education,
    TechSkill,
    SoftSkill,
    Language,
)


class ResumeView(ListView):
    """View for main (resume) page"""
    model = Configuration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_account'] = SocialAccount.objects.first()
        context['jumbotron'] = Jumbotron.objects.first()
        context['job'] = Job.objects.all()
        context['education'] = Education.objects.all()
        context['tech_skill'] = TechSkill.objects.all()
        context['soft_skill'] = SoftSkill.objects.all()
        context['language'] = Language.objects.all()
        context['menu_parent'] = Menu.objects.filter(icon_type='DD')
        context['menu_single'] = Menu.objects.filter(icon_type='N')
        context['menu_disabled'] = Menu.objects.filter(icon_type='DI')
        context['submenu'] = SubMenu.objects.all()
        return context
