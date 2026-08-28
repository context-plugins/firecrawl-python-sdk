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
from ..errors.map_urls_error import MapUrlsErrorBody, map_urls_error_mapper
from ..models.map_request import MapRequest, MapRequestDict
from ..models.map_response import MapResponse
from ..server.server import Server


class MappingApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MappingApiWithRawResponse(client, server, auth)

    def map_urls(
        self, body: MapRequest | MapRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> MapResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Map402Error1 | Map429Error1 |
                Map500Error1 | RawError``."""
        return self._with_raw_response.map_urls(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MappingApiWithRawResponse:
        return self._with_raw_response


class AsyncMappingApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMappingApiWithRawResponse(client, server, auth)

    async def map_urls(
        self, body: MapRequest | MapRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> MapResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Map402Error1 | Map429Error1 |
                Map500Error1 | RawError``."""
        return (await self._with_raw_response.map_urls(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncMappingApiWithRawResponse:
        return self._with_raw_response


class MappingApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def map_urls(
        self, body: MapRequest | MapRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MapResponse, MapUrlsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/map"),
            body=json_body[MapRequest | MapRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MapResponse],
            error_mapper=map_urls_error_mapper,
            request_options=request_options,
        )


class AsyncMappingApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def map_urls(
        self, body: MapRequest | MapRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MapResponse, MapUrlsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/map"),
            body=json_body[MapRequest | MapRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MapResponse],
            error_mapper=map_urls_error_mapper,
            request_options=request_options,
        )
