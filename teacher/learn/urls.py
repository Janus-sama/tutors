from django.urls import path
from learn import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = views.UserDetail.name),
]
