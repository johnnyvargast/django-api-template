from datetime import datetime

import pytz
from django.contrib.auth.models import User
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from apps.commons.utils import GenericDateTimeOperations


def block_token(token):
    token_payload = token_backend.decode(token)
    user = User.objects.get(id=token_payload.get("user_id"))
    created_at = GenericDateTimeOperations().get_current_datetime()
    expires_at = datetime.utcfromtimestamp(token_payload.get("exp")).replace(tzinfo=pytz.utc)
    jti = token_payload.get("jti")
    if not OutstandingToken.objects.filter(jti=jti).exists():
        outstanding_token = OutstandingToken.objects.create(
            user=user,
            jti=jti,
            token=token,
            created_at=created_at,
            expires_at=expires_at)
        BlacklistedToken.objects.get_or_create(token=outstanding_token)
