from django.urls import path
from blog import views

urlpatterns = [

    path('', views.post_iist, name='post_iist'),
]
