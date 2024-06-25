from django.urls import path


from dogblog.feedback.views import FeedbackCreateView

urlpatterns = [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
