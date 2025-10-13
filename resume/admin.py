from django.contrib import admin

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


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("title", "order")


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "icon_type",
    )


class SubMenuAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "parent",
        "order",
        "url",
    )


admin.site.register(Jumbotron)
admin.site.register(TechSkill)
admin.site.register(Job, JobAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(SocialAccount)
admin.site.register(Configuration)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
