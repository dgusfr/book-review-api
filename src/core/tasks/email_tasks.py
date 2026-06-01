from asgiref.sync import async_to_sync

from src.core.mail.mail_config import create_message, mail
from src.core.tasks.celery_app import c_app


@c_app.task()
def send_email(recipients: list[str], subject: str, body: str) -> None:
    message = create_message(
        recipients=recipients,
        subject=subject,
        body=body,
    )

    async_to_sync(mail.send_message)(message)
    print("Email sent")
