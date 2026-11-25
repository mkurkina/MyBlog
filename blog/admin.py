from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_checked')
    list_filter = ('is_checked',)
    search_fields = ('full_name', 'email', 'text')
    list_editable = ('is_checked',)