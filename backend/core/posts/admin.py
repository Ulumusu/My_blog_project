from django.contrib import admin
from .models import Post, Text


class TextGen(admin.TabularInline):
    model = Text
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {
             'fields': [
                 'title',
                 'beginning',
                 'main_picture',
                 'main_text'
             ]
         }
         ),
    ]
    inlines = [TextGen]


admin.site.register(Post, PostAdmin)