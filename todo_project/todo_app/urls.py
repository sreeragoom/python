from django.contrib import admin
from django.urls import path, include

from todo_app import views


urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cvbhome/',views.TasklistView.as_view(),name='cvbhome'),
    path('cvbdetails/<int:pk>/',views.DetailView.as_view(),name='cvbdetails'),
    path('cvbupdate/<int:pk>/',views.DetailView.as_view(),name='cvbupdate'),
    path('cvbdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvbdelete')
]