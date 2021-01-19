from django.contrib import admin
from .models import *

# Register your models here.


class InlineImage(admin.TabularInline):
    model = CatPhoto


class CatPostAdmin(admin.ModelAdmin):
    inlines = [InlineImage, ]


admin.site.register(CatPost, CatPostAdmin)
