from django.contrib import admin
from .models import Job, Education


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start', 'end',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'university', 'start', 'end',)


admin.site.register(Job, JobAdmin)
admin.site.register(Education, EducationAdmin)
