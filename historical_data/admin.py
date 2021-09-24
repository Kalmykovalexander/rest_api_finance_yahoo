from django.contrib import admin
from .models import FinanceData

class PanelAdmin(admin.ModelAdmin):
    list_display = ['id', 'symbol', 'date']
    list_display_links = ['id', 'symbol', 'date']
    search_fields = ['id', 'symbol', 'date']


admin.site.register(FinanceData, PanelAdmin)
