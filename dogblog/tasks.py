from celery import shared_task

from dogblog.feedback.email import send_contact_email_message


@shared_task
def email_message_task(subject, email, content, ip, user_id):
    return send_contact_email_message(subject, email, content,
                                      ip, user_id)
