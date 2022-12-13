from django.contrib import admin

from enterprise.models import Enterprise, Employee, CardEmployee

admin.site.register(Employee)
admin.site.register(Enterprise)
admin.site.register(CardEmployee)
