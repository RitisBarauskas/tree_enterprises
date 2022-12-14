from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from enterprise.models import Enterprise, Employee, CardEmployee


class EnterpriseAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"name": ("description",)}

admin.site.register(Employee)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(CardEmployee)
