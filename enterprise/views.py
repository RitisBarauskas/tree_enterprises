from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from enterprise.models import CardEmployee, Enterprise


class EnterpriseListView(ListView):
    model = Enterprise
    template_name = "enterprise/enterprises.html"

    def get_queryset(self):
        return Enterprise.objects.annotate(employees=Count('cards'))


class EmployeeByEnterpriseView(ListView):
    context_object_name = 'employees'
    template_name = 'enterprise/employees.html'

    def get_queryset(self):
        self.enterprise = get_object_or_404(Enterprise, id=self.kwargs['id'])
        queryset = CardEmployee.objects.filter(enterprise=self.enterprise)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.enterprise

        return context