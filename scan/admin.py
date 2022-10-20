from django.contrib import admin
from .models import Job, Node


@admin.action(description='Set status to none')
def make_none(modeladmin, request, queryset):
    """Change selected job's status to none"""
    rows_updated = queryset.update(status='n')
    if rows_updated == 1:
        message_bit = "Job's status changed to none."
    else:
        message_bit = "Jobs' status changed to none."
    modeladmin.message_user(request, "{} {}".format(rows_updated, message_bit))


class NodeAdmin(admin.ModelAdmin):
    ordering = ['-node_type', '-is_active', 'location']
    list_display = ['node_type', 'location', 'url', 'is_active']


class JobsAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'id',
        'add_time',
        'start_time',
        'update_time',
        'command',
        'node',
        'status',
        'uuid',
        'url',
        'result',
    ]
    list_filter = ['status', 'command', 'add_time', 'node']
    search_fields = [
        'id',
        'add_time',
        'start_time',
        'update_time',
        'result',
        'uuid',
        'url',
    ]
    actions = [make_none]


admin.site.register(Node, NodeAdmin)
admin.site.register(Job, JobsAdmin)
