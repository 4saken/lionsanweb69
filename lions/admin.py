from django.contrib import admin
from . models import Lion


class LionAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_count')


admin.site.register(Lion, LionAdmin)
