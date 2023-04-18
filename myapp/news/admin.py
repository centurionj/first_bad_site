from django.contrib import admin

from .models import Articles

# Register your models here.

# class ArticlesAdmin(admin.ModelAdmin):
#     list_display = ('title', 'anons', 'date')
#     list_display_links = ('title', 'anons')
#     search_fields = ('title', 'anons')
#
# admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Articles)
