from django.contrib import admin
from .models import Article, Comment

class commentInline(admin.TabularInline):
    model = Comment
    extra = 0 # this cancels the extra lines of comments added by default

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        commentInline,
    ]

    list_display = [
        "title",
        #"body",
        "author",
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)