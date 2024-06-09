from django.urls import path

from dogblog.comments.views import IndexCommentView, CreateCommentView

urlpatterns = [
    path("", IndexCommentView.as_view(), name="index_comment"),
    path("<int:pk>/create/", CreateCommentView.as_view(), name="create_comment"),
]
