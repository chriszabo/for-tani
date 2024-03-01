from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_sheet_list, name='character_sheet_list'),
    path('edit/<int:pk>/', views.character_sheet_edit, name='character_sheet_edit'),
    path('new/', views.character_sheet_new, name='character_sheet_new'),
]