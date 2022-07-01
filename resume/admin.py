from django.contrib import admin
from .models import (
    Job,
    Education,
    TechSkill,
    SoftSkill,
    Language,
    Jumbotron,
    SocialAccount,
    Configuration,
    Menu,
    SubMenu
)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start', 'end',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'university', 'start', 'end',)


class TechSkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order', 'url',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'icon_type',)


admin.site.register(Job, JobAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(TechSkill, TechSkillAdmin)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(Language, LanguageSkillAdmin)
admin.site.register(Jumbotron)
admin.site.register(SocialAccount)
admin.site.register(Configuration)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
