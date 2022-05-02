from django.views.generic.list import ListView
from resume.models import Job, Education, TechSkill, Jumbotron


class JobListView(ListView):
    """TEMP"""
    model = Job


class EducationListView(ListView):
    """TEMP"""
    model = Education


class TechSkillListView(ListView):
    """TEMP"""
    model = TechSkill


class JumbotronListView(ListView):
    """TEMP"""
    model = Jumbotron
