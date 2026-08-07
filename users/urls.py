from django.urls import path, include
from users.views import sign_up,sign_in,sign_out,active_user,admin_dashboard,Sign_in,ProfileView,change_password,PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.views import LogoutView,PasswordChangeDoneView

urlpatterns = [
    path('sign-up/',sign_up,name='sign-up'),
    # path('sign-in/',sign_in,name='sign-in'),
    path('sign-in/',Sign_in.as_view(),name='sign-in'),
    # path('sign-out/',sign_out,name='logout'),
    path('sign-out/',LogoutView.as_view(),name='logout'),
    path('activate/<int:id>/<str:token>/',active_user),
    path('admin/dashboard/',admin_dashboard,name='admin-dashboard'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/password-change',change_password.as_view(),name='change-password'),
    path('profile/password-change-done',PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),name='password_change_done'),
    path('reset-password/',PasswordResetView.as_view(),name='reset-password'),
    path('reset-password/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
]
