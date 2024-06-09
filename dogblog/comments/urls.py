from django.urls import path

from dogblog.comments.views import IndexCommentView

urlpatterns = [
    path("", IndexCommentView.as_view(), name="index_comment"),
]
