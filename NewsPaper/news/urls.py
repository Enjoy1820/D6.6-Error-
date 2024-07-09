from django.urls import path

from .views import Postlist, PostDetail

urlpatterns = [
    path('news/', Postlist.as_view(), name='post-list'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]