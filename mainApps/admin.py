from django.contrib import admin
from .models import *

# Register your models here.


class InlineImage(admin.TabularInline):
    model = CatPhoto


class CatPostAdmin(admin.ModelAdmin):
    inlines = [InlineImage, ]


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'email',
        'date_joined'
    )
    list_display_links = (
        'nickname',
        'email'
    )


admin.site.register(CatPost, CatPostAdmin)
admin.site.register(User, UserAdmin)
