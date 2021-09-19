from django.urls import path
from . import views

urlpatterns=[path("register/", views.register, name="register"),
path("login/", views.loggedin, name="login"),
path("logout/", views.loggedout, name="logout"),
path("update/",views.create_user,name="createuser"),
path("status/",views.status,name="status"),

path("home/", views.college, name="college"),
path("add/",views.CreateScholarship,name="createscholarship"),
path("application_form/<int:id>", views.application_form, name="application_form"),
path("display_form/<int:id>", views.display_scholarship, name="display_form"),
path("approved_applications/", views.approved_applications, name="approved_applications"),
path("pending_applications/", views.pending_applications, name="pending_applications"),
path("rejected_applications/", views.rejected_applications, name="rejected_applications"),
path("handle_admin/", views.handle_admin, name="handle_admin"),
path("student_application/<int:myid>/", views.student_application, name="student_application"),
path("application_status/accept/<int:myid>/",views.updateaccept,name="updateaccept"),
path("application_status/reject/<int:myid>/",views.updatereject,name="updatereject"),


]
