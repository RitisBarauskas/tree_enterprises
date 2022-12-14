from django.urls import path

from enterprise.views import (CardEmployeeDetail, EmployeeByEnterpriseView,
                              EnterpriseListView)

app_name = 'enterprises'

urlpatterns = [
    path(
        '<int:id>/',
        EmployeeByEnterpriseView.as_view(),
        name='employees-by-enterprises',
    ),
    path('employee/<int:id>/',
         CardEmployeeDetail.as_view(),
         name='employee-detail',
         ),
    path(
        '',
        EnterpriseListView.as_view(),
        name='enterprises-list',
    ),
]
