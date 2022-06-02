from django.contrib import admin
from django.urls import path,include
from Users import views

urlpatterns = [
    path('Login', views.login),
    path('Register', views.register),
    path('Logout',views.logout),
    path('User_View',views.User_view),
    path('User_Update',views.User_view),
    path('User_Update/<int:id>',views.User_update),
    path('User_Delete',views.User_view),
    path('User_Delete/<int:id>',views.User_delete),
]
