from nuevo_proyecto.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import TagListView, TagCreateView, TagDeleteView, PostbyTagView
from .views import CommentCreateView
from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginView, name = 'login'),
    path('registro/', views.registroView, name = 'registro'),
    path('logout/', views.logoutView, name = 'logout'),
    path('post/', PostListView.as_view(), name = 'post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name ='post_detail'),
    path('new/', PostCreateView.as_view(), name ='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
    path('tags/', TagListView.as_view(), name = 'tag_list'),
    path('newT/', TagCreateView.as_view(), name = 'tag_create'),
    # path('<int:pk>/editT/', TagUpdateView.as_view(), name = 'tag_edit'),
    path('<int:pk>/deleteT/', TagDeleteView.as_view(), name = 'tag_delete'),
    path('post_by_tag/<int:pk>/', PostbyTagView.as_view(), name = 'post_list_by_tag'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name = 'comment_create'),
    path('politica-cookies/', views.politica_cookies, name = 'politica_cookies'),
    path('weather/', views.weather, name ='weather'),
    path('recipe/', views.recipe, name ='recipe')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

