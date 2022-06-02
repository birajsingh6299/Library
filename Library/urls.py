from django.contrib import admin
from django.urls import path,include
from Library import views

urlpatterns = [
    path('Book_View', views.Book_view),
    path('Book_Update', views.Book_view),
    path('Book_Update/<int:id>',views.Book_update),
    path('Book_Create',views.Book_create),
    path('Book_Delete',views.Book_view),
    path('Book_Delete/<int:id>',views.Book_delete),
    path('Book_Return',views.Book_view),
    path('Book_Borrow',views.Book_view),
    path('Book_Return/<int:id>',views.Book_return),
    path('Book_Borrow/<int:id>',views.Book_borrow),
]
