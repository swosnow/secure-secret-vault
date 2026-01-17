from django.contrib import admin
from .models import RequestLog


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'method',
        'url',
        'response_status',
        'duration',
    )
    list_filter = ('method', 'response_status')
    search_fields = ('url',)
    ordering = ('-timestamp',)

# Register your models here.
