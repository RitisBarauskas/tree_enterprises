from django.urls import path

from enterprise.views import EnterpriseListView, EmployeeByEnterpriseView

app_name = 'enterprises'

urlpatterns = [
    path('', EnterpriseListView.as_view(), name='enterprises-list'),
    path('<int:id>/', EmployeeByEnterpriseView.as_view(), name='employees-by-enterprises'),
]
