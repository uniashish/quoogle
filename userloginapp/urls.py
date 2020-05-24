from django.conf.urls import url
from userloginapp import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'userloginapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name='activate'),
    path('activateconfirm/',views.activation_email_confirmation,name='confirm_activate_email')
]
