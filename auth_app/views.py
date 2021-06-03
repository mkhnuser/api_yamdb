from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.views.generic.base import View
from users.models import User
from http import HTTPStatus
import os


class EmailCodeVerification(View):
    """
    Отсылает письмо с кодом на email, который был указан в POST запросе,
    но только, если пользователь предоставил email и был зарегистрирован.
    """
    def post(self, request):
        user_email = request.POST.get('email')
        if not user_email:
            return HttpResponse('See you later, alligator!', status=HTTPStatus.BAD_REQUEST)

        try:
            user = User.objects.create(
                email=user_email
            )
        except Exception as e:
            print(e)
        else:
            user.email_user(
                subject='YamDB: Verification Code',
                message=default_token_generator.make_token(user),
                from_email=os.getenv('EMAIL_NAME'),
            )
            return HttpResponse('Verification code was sent. Please, check your email!', status=HTTPStatus.OK)
        return HttpResponse('Specified email already was registered.', status=HTTPStatus.BAD_REQUEST)
