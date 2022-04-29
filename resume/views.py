from django.views.generic.list import ListView
from resume.models import Job, Education, TechSkill


class JobListView(ListView):
    """TEMP"""
    model = Job


class EducationListView(ListView):
    """TEMP"""
    model = Education


class TechSkillListView(ListView):
    """TEMP"""
    model = TechSkill
