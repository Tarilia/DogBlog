from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

from ..tasks import email_message_task
from .forms import FeedbackForm
from .models import Feedback
from ..utils import get_client_ip


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_message = _('Your letter has been sent successfully')
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('index_articles')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            if self.request.user.is_authenticated:
                feedback.user = self.request.user
            email_message_task.delay(feedback.subject,
                                     feedback.email,
                                     feedback.content,
                                     feedback.ip_address,
                                     feedback.user_id)
        return super().form_valid(form)
