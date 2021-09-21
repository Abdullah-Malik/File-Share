"""
defines all the urls that Posts app is using
"""
from django.urls import path

from .views import (
    PostCreateView,
    PostDashboardView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostSearchView,
    PostUpdateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-home"),
    path(
        "dashboard/",
        PostDashboardView.as_view(),
        name="post-dashboard",
    ),
    path("search/", PostSearchView.as_view(), name="post-search"),
    path("file/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "file/<int:pk>/update/",
        PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "file/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("file/new/", PostCreateView.as_view(), name="post-create"),
]
