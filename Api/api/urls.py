from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')


urlpatterns=[
    path('students/',views.studentsView),   #function based view
    path('students/<int:pk>/', views.studentDetailsView),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>',views.EmployeeDetail.as_view()),

    path('',include(router.urls))

]