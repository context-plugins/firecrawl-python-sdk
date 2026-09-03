from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    raw_error_response,
)
from ..models.team_queue_status_response import TeamQueueStatusResponse
from ..server.server import Server


class Miscellaneous:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MiscellaneousWithRawResponse(client, server, auth)

    def get_queue_status(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamQueueStatusResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_queue_status(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MiscellaneousWithRawResponse:
        return self._with_raw_response


class AsyncMiscellaneous:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMiscellaneousWithRawResponse(client, server, auth)

    async def get_queue_status(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamQueueStatusResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_queue_status(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMiscellaneousWithRawResponse:
        return self._with_raw_response


class MiscellaneousWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_queue_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamQueueStatusResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/queue-status"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamQueueStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMiscellaneousWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_queue_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamQueueStatusResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/queue-status"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamQueueStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
