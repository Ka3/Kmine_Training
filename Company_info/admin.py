from django.contrib import admin

# Register your models here.

from Company_info.models import mas_company_profile,mas_states,mas_countries

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','postcode','company_name', 'address1', 'State','website')


admin.site.register(mas_states)
admin.site.register(mas_company_profile,CompanyAdmin)
admin.site.register(mas_countries)