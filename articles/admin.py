# articles/admin.py
from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)

admin.site.register(Article, ArticleAdmin)