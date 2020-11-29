from django.contrib import admin
from actions.models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('verb',)
