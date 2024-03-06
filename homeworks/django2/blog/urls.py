from django.urls import path
from blog import views

urlpatterns = [

    path('', views.post_iist, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('tags/<tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('author/<author_slug>/', views.posts_by_author, name='posts_by_author'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post')

]
