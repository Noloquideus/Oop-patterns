class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class UserService:
    def __init__(self, email_service):
        self.email_service = email_service

    def register_user(self, username):
        print(f"Registering user: {username}")
        self.email_service.send_email(username, "Welcome to our platform!")


# Создаем экземпляры зависимостей
email_service = EmailService()
user_service = UserService(email_service)

# Используем UserService для регистрации пользователя
user_service.register_user("John")