class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class ServiceLocator:
    _services = {}

    @staticmethod
    def register_service(service_name, service_instance):
        ServiceLocator._services[service_name] = service_instance

    @staticmethod
    def get_service(service_name):
        return ServiceLocator._services.get(service_name, None)


class UserService:
    def register_user(self, username):
        email_service = ServiceLocator.get_service('email_service')
        if email_service:
            email_service.send_email(username, "Welcome to our platform!")
        else:
            print("Email service is not registered.")


# Регистрируем зависимости в Service Locator
email_service = EmailService()
ServiceLocator.register_service('email_service', email_service)

# Создаем экземпляр UserService и используем его для регистрации пользователя
user_service = UserService()
user_service.register_user("John")