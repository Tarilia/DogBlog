from django.urls import path

from dogblog.users.views import CreateUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create_users"),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
