from django.contrib import admin

from core.models import CNAE, Company

# Register your models here.
class CompanyInline(admin.TabularInline):
    model = Company
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    model = Company
  
    fieldsets = [
        ("Identification", {"fields": ["cnpj", "legal_name", "trade_name"]}),
        ("Address", {"fields": ["address", "city", "state", "zip_code"]}),
        ("Fiscal", {"fields": ["cnae_main", "cnae_secondary"]})
    ]
    

class CNAEAdmin(admin.ModelAdmin):
    model = CNAE
    list_display = ('code', 'description')
    search_fields = ('code', 'description')
    Inlines = [CompanyInline]

admin.site.register(Company, CompanyAdmin)
admin.site.register(CNAE, CNAEAdmin)