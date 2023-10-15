from django.contrib import admin

from api.models import Employer

#create admin managers here
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('rank', 'company', 'industries', 'country_territory', 'publish_year')
    search_fields = ('rank', 'company', 'industries', 'country_territory', 'publish_year')
    ordering = ('rank', )

# Register your models here.
admin.site.register(Employer, EmployerAdmin)
