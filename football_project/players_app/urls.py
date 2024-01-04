from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from players_app import views
app_name='players_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/<int:player_id>/',views.about,name='about'),
    path('add/',views.add_players,name='add'),
    path('update/<int:p_id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]