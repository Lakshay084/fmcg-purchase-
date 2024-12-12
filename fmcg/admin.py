from django.contrib import admin
from .models import Supplier, Tender
from django.contrib.auth.hashers import make_password
from .models import ProductRate

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'username', 'name', 'company_name', 'mobile_number', 'address', 'created_at')
    search_fields = ('name', 'supplier_id', 'mobile_number')

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            obj.password = make_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('tender_id', 'supplier', 'product_name', 'quantity', 'rate_per_tonne', 'status', 'approved', 'delivery_date')
    list_filter = ('status', 'approved', 'delivery_date')
    search_fields = ('tender_id', 'supplier__name', 'product_name')

    actions = ['approve_tender', 'reject_tender']

    @admin.action(description="Approve selected tenders")
    def approve_tender(self, request, queryset):
        for tender in queryset:
            tender.status = 'Accepted'
            tender.approved = True
            tender.save()

    @admin.action(description="Reject selected tenders")
    def reject_tender(self, request, queryset):
        queryset.update(status='Rejected', approved=False)
        
@admin.register(ProductRate)
class ProductRateAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'rate_per_tonne')
    search_fields = ('product_name',)        

# Register your models here.
