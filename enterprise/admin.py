from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from enterprise.models import Enterprise, Employee, CardEmployee


class EnterpriseAdmin(MPTTModelAdmin):
    prepopulated_fields = {"name": ("description",)}

admin.site.register(Employee)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(CardEmployee)
