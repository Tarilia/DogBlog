from django.urls import path

from dogblog.article.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
