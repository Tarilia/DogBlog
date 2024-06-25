from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dogblog import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dogblog.article.urls')),
    path('users/', include('dogblog.users.urls')),
    path('comments/', include('dogblog.comments.urls')),
    path('feedback/', include('dogblog.feedback.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
