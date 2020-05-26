from django.conf.urls import url
from userloginapp import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
app_name = 'userloginapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name='activate'),
    path('activateconfirm/',views.activation_email_confirmation,name='confirm_activate_email'),

    #path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    #path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    #path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
