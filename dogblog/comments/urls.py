from django.urls import path

from dogblog.comments.views import (IndexCommentView, CreateCommentView,
                                    UpdateCommentView, DeleteCommentView)

urlpatterns = [
    path("", IndexCommentView.as_view(), name="index_comment"),
    path("<int:pk>/create/", CreateCommentView.as_view(),
         name="create_comment"),
    path("update/<int:pk>/", UpdateCommentView.as_view(),
         name="update_comment"),
    path("delete/<int:pk>/", DeleteCommentView.as_view(),
         name="delete_comment"),
]
