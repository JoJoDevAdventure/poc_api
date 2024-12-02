from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at')  # Fields to display in the list view
    search_fields = ('title', 'description')              # Fields to search
    list_filter = ('created_at',)                         # Fields to filter
    ordering = ('-created_at',)                           # Default ordering