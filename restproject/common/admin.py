# -*- coding: utf-8 -*-
from django.contrib import admin

from models import BackScratcher


class BackScratcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price')
    list_filter = ('size', )
    search_fields = ('name', 'size', 'price', 'description')
    limit = 40
admin.site.register(BackScratcher, BackScratcherAdmin)