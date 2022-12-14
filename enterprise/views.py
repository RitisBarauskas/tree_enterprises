from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from enterprise.models import CardEmployee, Enterprise


class EnterpriseListView(ListView):
    """
    Список компаний.
    """
    model = Enterprise
    template_name = "enterprise/enterprises.html"

    def get_queryset(self):
        return Enterprise.objects.annotate(employees=Count('cards'))


class EmployeeByEnterpriseView(ListView):
    """
    Список сотрудников компании
    """
    context_object_name = 'employees'
    template_name = 'enterprise/employees.html'

    def get_queryset(self):
        self.enterprise = get_object_or_404(Enterprise, id=self.kwargs['id'])

        return CardEmployee.objects.filter(enterprise=self.enterprise)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.enterprise

        return context


class CardEmployeeDetail(DetailView):
    """
    Карточка сотрудника
    """
    model = CardEmployee
    context_object_name = 'card_employee'
    template_name = 'enterprise/employee_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            CardEmployee.objects.select_related('employee'),
            id=self.kwargs.get("id"),
        )
