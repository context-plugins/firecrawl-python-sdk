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
    param,
    raw_error_response,
)
from ..models.enums.endpoint1 import Endpoint1OrStr
from ..models.team_activity_response import TeamActivityResponse
from ..server.server import Server


class Account:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountWithRawResponse(client, server, auth)

    def get_activity(
        self,
        *,
        endpoint: Endpoint1OrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamActivityResponse:
        """Lists your team's recent API activity from the last 24 hours. Returns metadata about each job including the
        job ID, which can be used with the corresponding GET endpoint (e.g. GET /crawl/{id}) to retrieve full results.
        Supports cursor-based pagination and filtering by endpoint.

        Args:
            endpoint: Filter by endpoint
            limit: Maximum number of results per page
            cursor: Cursor for pagination. Use the cursor value from the previous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_activity(
            endpoint=endpoint, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountWithRawResponse:
        return self._with_raw_response


class AsyncAccount:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountWithRawResponse(client, server, auth)

    async def get_activity(
        self,
        *,
        endpoint: Endpoint1OrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TeamActivityResponse:
        """Lists your team's recent API activity from the last 24 hours. Returns metadata about each job including the
        job ID, which can be used with the corresponding GET endpoint (e.g. GET /crawl/{id}) to retrieve full results.
        Supports cursor-based pagination and filtering by endpoint.

        Args:
            endpoint: Filter by endpoint
            limit: Maximum number of results per page
            cursor: Cursor for pagination. Use the cursor value from the previous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_activity(
                endpoint=endpoint, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountWithRawResponse:
        return self._with_raw_response


class AccountWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_activity(
        self,
        *,
        endpoint: Endpoint1OrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamActivityResponse, RawError]:
        """Lists your team's recent API activity from the last 24 hours. Returns metadata about each job including the
        job ID, which can be used with the corresponding GET endpoint (e.g. GET /crawl/{id}) to retrieve full results.
        Supports cursor-based pagination and filtering by endpoint.

        Args:
            endpoint: Filter by endpoint
            limit: Maximum number of results per page
            cursor: Cursor for pagination. Use the cursor value from the previous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/activity"),
            query_params=[
                param[Endpoint1OrStr | None]("endpoint", endpoint),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamActivityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAccountWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_activity(
        self,
        *,
        endpoint: Endpoint1OrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TeamActivityResponse, RawError]:
        """Lists your team's recent API activity from the last 24 hours. Returns metadata about each job including the
        job ID, which can be used with the corresponding GET endpoint (e.g. GET /crawl/{id}) to retrieve full results.
        Supports cursor-based pagination and filtering by endpoint.

        Args:
            endpoint: Filter by endpoint
            limit: Maximum number of results per page
            cursor: Cursor for pagination. Use the cursor value from the previous response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/activity"),
            query_params=[
                param[Endpoint1OrStr | None]("endpoint", endpoint),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamActivityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
