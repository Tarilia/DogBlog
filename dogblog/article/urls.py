from django.urls import path

from dogblog.article.views import (IndexArticlesView, CreateArticlesView,
                                   DetailArticlesView, UpdateArticlesView,
                                   DeleteArticlesView, FilterCategoryView,
                                   FilterTagView)

urlpatterns = [
    path('', IndexArticlesView.as_view(), name='index_articles'),
    path("create/", CreateArticlesView.as_view(), name="create_articles"),
    path("<slug:slug>/", DetailArticlesView.as_view(), name="detail_articles"),
    path("<slug:slug>/update/", UpdateArticlesView.as_view(),
         name="update_articles"),
    path("<slug:slug>/delete/", DeleteArticlesView.as_view(),
         name="delete_articles"),
    path('category/<slug:slug>/', FilterCategoryView.as_view(),
         name="category_articles"),
    path('tags/<str:tag>/', FilterTagView.as_view(), name="tags_articles"),
]
