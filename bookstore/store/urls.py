from django.urls import path
from .import views

urlpatterns = [
    path('users/', views.showUserList),
    path('users/<int:pk>', views.RequestedUser),
    path('books/', views.showBookList),
    path('books/<int:pk>', views.RequestedBook),
    path('books/add/', views.addBooks),
    path('books/borrow/<int:pk>', views.borrowBooks),
    path('books/history/', views.borrowingHistory),
]