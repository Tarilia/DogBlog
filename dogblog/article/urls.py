from django.urls import path

from dogblog.article.views import IndexPageView

urlpatterns = [
    path('', IndexArticlesView.as_view(), name='index_articles'),
    path("create/", CreateArticlesView.as_view(), name="create_articles"),
    path("<slug:slug>/", DetailArticlesView.as_view(), name="detail_articles"),
]
