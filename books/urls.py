# books/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),  # URL for book details
    path('add/', views.book_add, name='book_add'),  # URL for adding a new book
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),  # New URL for deleting a book
]

# Add this at the end to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
