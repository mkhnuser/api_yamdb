from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.core.mail import send_mail
from users.models import User
from http import HTTPStatus
import os
import uuid


class EmailCodeVerificationView(View):
    def post(self, request):
        user_email = request.POST.get('email')

        if not user_email:
            return HttpResponse(
                'See you later, alligator! Please, specify your email.',
                status=HTTPStatus.BAD_REQUEST
            )

        user_uuid = uuid.uuid4()

        try:
            send_mail(
                subject='YamDB: Verification Code',
                message=str(user_uuid),
                from_email=os.getenv('EMAIL_NAME'),
                recipient_list=[str(user_email)],
                fail_silently=False
            )
        except Exception:
            return HttpResponse(
                'We have some troubles with email sending. Please, try later!',
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        _, is_created = User.objects.get_or_create(
            email=user_email,
            uuid_field=user_uuid
        )

        if not is_created:
            return HttpResponse(
                'Specified email already was registered.',
                status=HTTPStatus.BAD_REQUEST
            )
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
                'See you later, alligator! Please, specify your email.',
                status=HTTPStatus.BAD_REQUEST
            )

        user = get_object_or_404(User, email=user_email)

        is_valid_user = user_email == user.email
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
