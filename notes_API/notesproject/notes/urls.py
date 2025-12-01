from django.urls import path
from notes import views

urlpatterns = [
    # Note endpoints
    path('notes/', views.note_list, name='note-list'),
    path('notes/<int:pk>/', views.note_detail, name='note-detail'),
    
    # Tag endpoints
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<int:pk>/', views.tag_detail, name='tag-detail'),
]