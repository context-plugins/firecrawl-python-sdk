from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
)
from ..errors.get_threat_protection_error import GetThreatProtectionErrorBody, get_threat_protection_error_mapper
from ..errors.update_threat_protection_error import (
    UpdateThreatProtectionErrorBody,
    update_threat_protection_error_mapper,
)
from ..models.team_threat_protection_request import TeamThreatProtectionRequest, TeamThreatProtectionRequestDict
from ..models.team_threat_protection_response import TeamThreatProtectionResponse
from ..server.server import Server


class ThreatProtection:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ThreatProtectionWithRawResponse(client, server, auth)

    def get_threat_protection(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> TeamThreatProtectionResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Effective threat protection policy for the team's organization.

        Raises:
            ApiError: Threat protection is not enabled for this team, or a request override was sent while overrides are
                disabled. ``error`` is ``RawError``."""
        return self._with_raw_response.get_threat_protection(request_options=request_options).unwrap()

    def update_threat_protection(
        self,
        body: TeamThreatProtectionRequest | TeamThreatProtectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamThreatProtectionResponse:
        """Full-document update. Unspecified fields reset to defaults. Enterprise feature, team admins only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Effective threat protection policy for the team's organization.

        Raises:
            ApiError: Invalid policy document. Threat protection is not enabled for this team, or a request override was
                sent while overrides are disabled. ``error`` is ``RawError``."""
        return self._with_raw_response.update_threat_protection(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ThreatProtectionWithRawResponse:
        return self._with_raw_response


class AsyncThreatProtection:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncThreatProtectionWithRawResponse(client, server, auth)

    async def get_threat_protection(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> TeamThreatProtectionResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Effective threat protection policy for the team's organization.

        Raises:
            ApiError: Threat protection is not enabled for this team, or a request override was sent while overrides are
                disabled. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_threat_protection(request_options=request_options)).unwrap()

    async def update_threat_protection(
        self,
        body: TeamThreatProtectionRequest | TeamThreatProtectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamThreatProtectionResponse:
        """Full-document update. Unspecified fields reset to defaults. Enterprise feature, team admins only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Effective threat protection policy for the team's organization.

        Raises:
            ApiError: Invalid policy document. Threat protection is not enabled for this team, or a request override was
                sent while overrides are disabled. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_threat_protection(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncThreatProtectionWithRawResponse:
        return self._with_raw_response


class ThreatProtectionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_threat_protection(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamThreatProtectionResponse, GetThreatProtectionErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/threat-protection"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamThreatProtectionResponse],
            error_mapper=get_threat_protection_error_mapper,
            request_options=request_options,
        )

    def update_threat_protection(
        self,
        body: TeamThreatProtectionRequest | TeamThreatProtectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamThreatProtectionResponse, UpdateThreatProtectionErrorBody]:
        """Full-document update. Unspecified fields reset to defaults. Enterprise feature, team admins only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/team/threat-protection"),
            body=json_body[TeamThreatProtectionRequest | TeamThreatProtectionRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamThreatProtectionResponse],
            error_mapper=update_threat_protection_error_mapper,
            request_options=request_options,
        )


class AsyncThreatProtectionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_threat_protection(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamThreatProtectionResponse, GetThreatProtectionErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/threat-protection"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamThreatProtectionResponse],
            error_mapper=get_threat_protection_error_mapper,
            request_options=request_options,
        )

    async def update_threat_protection(
        self,
        body: TeamThreatProtectionRequest | TeamThreatProtectionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamThreatProtectionResponse, UpdateThreatProtectionErrorBody]:
        """Full-document update. Unspecified fields reset to defaults. Enterprise feature, team admins only.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/team/threat-protection"),
            body=json_body[TeamThreatProtectionRequest | TeamThreatProtectionRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamThreatProtectionResponse],
            error_mapper=update_threat_protection_error_mapper,
            request_options=request_options,
        )
