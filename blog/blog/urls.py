from django.urls import path
from .views import PostListView, PostDetailView, CategoryDetailView, TutorialListView, TutorialDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
	path('tutorials/', TutorialListView.as_view(), name='blog-tutorials'),
	path('tutorials/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )