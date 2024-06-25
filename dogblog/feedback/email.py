from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def send_contact_email_message(subject, email, content, ip, user_id):
    user = get_user_model().objects.get(id=user_id) if user_id else None
    message = render_to_string('feedback/feedback_email.html',
                               {'email': email,
                                'content': content,
                                'ip': ip,
                                'user': user})
    email = EmailMessage(subject, message, settings.SERVER_EMAIL,
                         [settings.EMAIL_ADMIN])
    email.send(fail_silently=False)
