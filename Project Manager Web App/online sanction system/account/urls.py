from account import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name="account"
urlpatterns=[

path("",views.my_view,name="user_login"),
path("change_your_password/",views.change_password,name="change_password"),

path("Boss/homepage/",views.Boss_homepage,name="homepage"),
path("Boss/edit_profile/",views.Boss_edit_profile,name="edit_profile"),
path("Boss/view_profile/",views.Boss_view_profile,name="view_profile"),
path("Boss/assign_project/",views.assign_project,name="assign_project"),
path("Boss/review_projects/",views.review_projects,name="review_projects"),
path("Boss/logout/",views.user_logout,name="user_logout"),

path("Employee/homepage/",views.Employee_homepage,name="homepage"),
path("Employee/edit_profile/",views.Employee_edit_profile,name="edit_profile"),
path("Employee/view_profile/",views.Employee_view_profile,name="view_profile"),
path("Employee/project_list/",views.project_list,name="project_list"),
path("Employee/project_submit/<id>/",views.project_submit, name='project_submit'),
path("Employee/logout/",views.user_logout,name="user_logout"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
