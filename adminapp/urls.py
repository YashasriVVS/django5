from django.urls import path
from .import views

urlpatterns = [
   path('adminhome',views.adminhome,name="adminhome"),
   path('adminlogout',views.logout,name="adminlogout"),
   path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
   path("viewstudents",views.viewstudents,name="viewstudents"),
   path("viewcourses",views.viewcourses,name="viewcourses"),
   path("viewfaculty",views.viewfaculty,name="viewfaculty"),

]
