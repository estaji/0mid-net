from django.views.generic.list import ListView
from core.models import CoreConfig, Menu, SubMenu
from resume.models import (
    ResumeConfig,
    SocialAccount,
    Jumbotron,
    Job,
    Education,
    TechSkill,
    TechSkillText,
    SoftSkill,
    Language,
)


class ResumeView(ListView):
    """View for main (resume) page"""
    model = ResumeConfig

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_account'] = SocialAccount.objects.first()
        context['jumbotron'] = Jumbotron.objects.first()
        context['job'] = Job.objects.all()
        context['education'] = Education.objects.all()
        context['tech_skill_accordion'] = TechSkill.objects.all()
        context['tech_skill_text'] = TechSkillText.objects.first()
        context['soft_skill'] = SoftSkill.objects.all()
        context['language'] = Language.objects.all()
        context['core_conf'] = CoreConfig.objects.all()
        context['menu_parent'] = Menu.objects.filter(icon_type='DD')
        context['menu_single'] = Menu.objects.filter(icon_type='N')
        context['menu_disabled'] = Menu.objects.filter(icon_type='DI')
        context['submenu'] = SubMenu.objects.all()
        return context
