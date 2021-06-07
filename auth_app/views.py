from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.core.mail import send_mail
from users.models import User
from http import HTTPStatus
from pprint import pprint
import os
import uuid


class EmailCodeVerificationView(View):
    def post(self, request):
        user_email = request.POST.get('email')

        if not user_email:
            return HttpResponse(
                'See you later, alligator!',
                status=HTTPStatus.BAD_REQUEST
            )

        try:
            user_uuid = uuid.uuid4()
            send_mail(
                subject='YamDB: Verification Code',
                message=str(user_uuid),
                from_email=os.getenv('EMAIL_NAME'),
                recipient_list=[str(user_email)]
            )
        except Exception as e:
            pprint(e)
            return HttpResponse(
                'We have some troubles with email sending. Please, try later!',
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        # Регистрируем пользователя !только! в том случае,
        # если письмо было отправлено (see else in try/except statements).
        # Кстати, именно из-за этого был использован uuid - его можно
        # генерировать без непосредственной модели юзера.
        else:
            try:
                User.objects.create(
                    email=user_email,
                    uuid_field=user_uuid
                )
            except Exception as e:
                pprint(e)
                return HttpResponse(
                        'Specified email already was registered.',
                        status=HTTPStatus.BAD_REQUEST
                )
            else:
                return HttpResponse(
                    'Verification code was sent. Please, check your email!',
                    status=HTTPStatus.OK
                )


class AuthenticationView(View):
    def post(self, request):
        user_email = request.POST.get('email')
        confirmation_code = request.POST.get('confirmation_code')

        if not user_email or not confirmation_code:
            return HttpResponse(
                'See you later, alligator!',
                status=HTTPStatus.BAD_REQUEST
            )

        try:
            user = User.objects.get(email=user_email)
        except Exception as e:
            pprint(e)
            return HttpResponse(
                'User with specified email does not exist!',
                status=HTTPStatus.BAD_REQUEST
            )

        is_valid_user = user_email == user.email
        # Изменяем тип поля uuid_field,
        # т.к. по умолчанию это UUID class instance
        is_valid_confirmation_code = str(user.uuid_field) == confirmation_code

        if is_valid_user and is_valid_confirmation_code:
            return JsonResponse(
                TokenPairView.get_tokens_for_user(user=user),
                status=HTTPStatus.OK
            )
        return HttpResponse(
            'Error! You passed wrong credentials.',
            status=HTTPStatus.BAD_REQUEST
        )


class TokenPairView:
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return data
