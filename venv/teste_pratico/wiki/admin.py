from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "autor", "created", "updated", "status", "setor")
    prepopulated_fields = {"slug": ("title",)}