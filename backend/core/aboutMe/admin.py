from django.contrib import admin
from .models import Part, AboutMe


class Textgen(admin.TabularInline):
    model = Part
    extra = 1


class AboutMeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['beginning']}),
    ]
    inlines = [Textgen]


# Register your models here.
admin.site.register(AboutMe, AboutMeAdmin)