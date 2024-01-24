from django.urls import path

from . import views

urlpatterns = [
    
    path('register/', views.register, name = "register"),
    path('login/', views.user_login, name = "user_login"),
    path('profile/', views.profile, name = "profile"),
    path('logout/', views.user_logout , name = 'logout'),
    path('passchng/', views.pass_change , name = 'passchng'),
    path('updateprof/', views.profile_upd , name = 'updatepf'),


]