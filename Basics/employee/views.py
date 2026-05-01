from django.shortcuts import render, get_object_or_404
from employee.models import Employee
from django.http import HttpResponse
# Create your views here.

def employee_detail(request, pk):
    # try:
    #     employee=Employee.objects.get(pk=pk)
    # except:
    #     raise Http404

    employee=get_object_or_404(Employee,pk=pk)
   
    # return HttpResponse(employee)
    context={
        'employee':employee
    }

    return render(request,'employee_detail.html',context)