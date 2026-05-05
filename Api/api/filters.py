import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_name=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')

    ##for int id  i.e 0,  1
    #emp_id=django_filters.RangeFilter(field_name='emp_id')

    ##char id range i.e  emp002
    id_min=django_filters.CharFilter(method='filter_by_id_range',label='From Emp Id')
    id_max=django_filters.CharFilter(method='filter_by_id_range',label='To Emp Id')



    class Meta:
        model=Employee
        fields=['designation','emp_name']


    def filter_by_id_range(self,queryset,name,value):
        if name=='id_min':
            return queryset.filter(emp_id__gte=value)
        elif name=='id_max':
            return queryset.filter(emp_id_lte=value)
        return queryset

  
        

