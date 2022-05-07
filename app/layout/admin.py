from django.contrib import admin

from .models import Page, Navigation, Style


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    pass


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    pass
