from django.contrib import admin

from .models import (
    Education,
    Job,
    Jumbotron,
    Language,
    ResumeConfig,
    SocialAccount,
    SoftSkill,
    TechSkill,
    TechSkillText,
)


class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "start",
        "end",
    )


class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "level",
        "university",
        "start",
        "end",
    )


class TechSkillAdmin(admin.ModelAdmin):
    list_display = ("title", "order")


class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ("title", "order")


class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = ("title", "order")


admin.site.register(Job, JobAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(TechSkill, TechSkillAdmin)
admin.site.register(TechSkillText)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(Language, LanguageSkillAdmin)
admin.site.register(Jumbotron)
admin.site.register(SocialAccount)
admin.site.register(ResumeConfig)
