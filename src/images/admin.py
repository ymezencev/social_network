from django.contrib import admin

from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'image', 'created_at']
    list_filter = ['created_at']
