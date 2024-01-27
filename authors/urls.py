from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('register/', views.register, name = "register"),
    # path('login/', views.user_login, name = "user_login"),
    path('login/', views.UserLoginView.as_view(), name = "user_login"),
    path('profile/', views.profile, name = "profile"),
    path('logout/', views.user_logout , name = 'logout'),
    # path('logout/', views.LogoutView.as_view() , name = 'logout'),
    path('passchng/', views.pass_change , name = 'passchng'),
    path('updateprof/', views.profile_upd , name = 'updatepf'),


]