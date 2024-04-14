from django.contrib import admin
from django.urls import path, include

from dogblog.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    # path('users/', include('dogblog.users.urls')),
]
