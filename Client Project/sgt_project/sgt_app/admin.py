from django.contrib import admin
from sgt_app.models import SGTEntries

# Register your models here.
@admin.register(SGTEntries)
class EntriesAdmin(admin.ModelAdmin):
    list_display = ['date','firm_name','lr_no','vehicle_no','location',
                    'amount','cash','diesel','rtgs','commission', 'total_balance', 'status']
    list_filter = ['vehicle_no','date','lr_no']
    search_fields = ('vehicle_no','date','location','lr_no',)
    list_editable = ['amount','cash','diesel','rtgs','commission']
    prepopulated_fields = {'slug': ('vehicle_no',)}