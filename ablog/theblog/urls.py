from django.urls import path
from . import views

app_name = 'theblog'

urlpatterns = [
    path('', views.IndexPost.as_view(), name='homepage'),
    path('article/<int:pk>', views.DetailPost.as_view(), name='detailpost'),
    path('addpost/', views.AddPost.as_view(), name='add_post'),
    path('article/edit/<int:pk>', views.EditUpdatePost.as_view(), name='edit_post'),
    path('article/<int:pk>/remove', views.DeletePost.as_view(), name='remove_post'),
]
