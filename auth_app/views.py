from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from users.models import User
from http import HTTPStatus
import os


class EmailCodeVerificationView(View):
    def post(self, request):
        user_email = request.POST.get('email')

        if not user_email:
            return HttpResponse(
                'See you later, alligator!',
                status=HTTPStatus.BAD_REQUEST
            )

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
            return HttpResponse(
                'Verification code was sent. Please, check your email!',
                status=HTTPStatus.OK
            )
        return HttpResponse(
                'Specified email already was registered.',
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
            print(e)

        
        is_valid_user = user_email == user.email
        is_valid_confirmation_code = default_token_generator.check_token(
            user=user,
            token=confirmation_code
        )

        if is_valid_user and is_valid_confirmation_code:
            return JsonResponse(
                TokenPairView.get_tokens_for_user(user=user),
                status=HTTPStatus.OK
            )
        return HttpResponse('Error!', status=HTTPStatus.BAD_REQUEST)
