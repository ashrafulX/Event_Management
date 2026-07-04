from django.urls import path, include
from users.views import sign_up,sign_in,sign_out,active_user,admin_dashboard
urlpatterns = [
    path('sign-up/',sign_up,name='sign-up'),
    path('sign-in/',sign_in,name='sign-in'),
    path('sign-out/',sign_out,name='logout'),
    path('activate/<int:id>/<str:token>/',active_user),
    path('admin/dashboard/',admin_dashboard,name='admin-dashboard'),
]
