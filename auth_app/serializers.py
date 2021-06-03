# from rest_framework_simplejwt.serializers import TokenObtainSerializer
# from rest_framework import exceptions, serializers
# from .settings import USER_AUTHENTICATION_RULE
# from django.contrib.auth import get_user_model
# 
# 
# class CustomTokenObtainSerializer(TokenObtainSerializer):
#     user_email_field = get_user_model().EMAIL_FIELD
# 
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
# 
#         self.fields[self.user_email_field] = serializers.CharField()
# 
#     def validate(self, attrs):
#         authenticate_kwargs = {
#             self.user_email_field: attrs[self.user_email_field],
#             'confirmation_code': attrs['confirmation_code'],
#         }
#         try:
#             authenticate_kwargs['request'] = self.context['request']
#         except KeyError:
#             pass
# 
#         self.user = authenticate(**authenticate_kwargs)
# 
#         if not api_settings.USER_AUTHENTICATION_RULE(self.user):
#             raise exceptions.AuthenticationFailed(
#                 self.error_messages['no_active_account'],
#                 'no_active_account',
#             )
# 
#         return {}
# 
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
# 
#         token['email'] = user.email
# 
#         return token
