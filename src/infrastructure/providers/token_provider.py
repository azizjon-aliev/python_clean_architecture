from rest_framework_simplejwt.tokens import RefreshToken

from src.application.common.contracts.providers.token_provider import TokenProviderInterface
from src.application.common.exceptions.authentication_exceptions import EntityInvalidCredentialsException
from src.domain.entities.account import User
from src.infrastructure.models import User as UserModel
from rest_framework_simplejwt.exceptions import TokenError

class TokenProvider(TokenProviderInterface):

    def get_token_output(self, refresh: RefreshToken) -> dict:
        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }

    def get_token(self, user: User) -> dict:
        user_object = UserModel.objects.get(id=user.user_id)
        refresh = RefreshToken.for_user(user_object)
        output = self.get_token_output(refresh)
        return output

    def verify_refresh_token(self, token: str) -> dict:
        try:
            refresh = RefreshToken(token)
        except TokenError:
            raise EntityInvalidCredentialsException("Refresh token has expired")
        output = self.get_token_output(refresh)
        return output
