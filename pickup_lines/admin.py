from django.contrib import admin
from .models import PickupLine

@admin.register(PickupLine)
class PickupLineAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('text',)
    ordering = ('-created_at',)
    list_per_page = 20
    
    fieldsets = (
        ('Pickup Line Details', {
            'fields': ('text', 'category')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-created_at')