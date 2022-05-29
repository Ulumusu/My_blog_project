from django.contrib import admin
from .models import Resume, Competence


# Register your models here.
class ExperienceAdmin(admin.StackedInline):
    model = Competence
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['main_photo',
                     'name_surname',
                     'email_info']}),
    ]
    inlines = [ExperienceAdmin]


admin.site.register(Resume, ResumeAdmin)