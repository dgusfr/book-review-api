from src.core.mail.mail_config import create_message, mail


class MailService:
    async def send_message(
        self,
        recipients: list[str],
        subject: str,
        body: str,
    ) -> None:
        message = create_message(
            recipients=recipients,
            subject=subject,
            body=body,
        )
        await mail.send_message(message)
