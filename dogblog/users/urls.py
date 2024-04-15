from django.urls import path

from dogblog.users.views import (CreateUserView, LoginUserView, LogoutUserView,
                                 UpdateUserView, DeleteUserView)

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create_users"),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="update_users"),
    path("<int:pk>/delete/", DeleteUserView.as_view(), name="delete_users"),
]
