from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_credit_usage_error import GetCreditUsageErrorBody, get_credit_usage_error_mapper
from ..errors.get_historical_credit_usage_error import (
    GetHistoricalCreditUsageErrorBody,
    get_historical_credit_usage_error_mapper,
)
from ..errors.get_historical_token_usage_error import (
    GetHistoricalTokenUsageErrorBody,
    get_historical_token_usage_error_mapper,
)
from ..errors.get_token_usage_error import GetTokenUsageErrorBody, get_token_usage_error_mapper
from ..models.team_credit_usage_historical_response import TeamCreditUsageHistoricalResponse
from ..models.team_credit_usage_response import TeamCreditUsageResponse
from ..models.team_token_usage_historical_response import TeamTokenUsageHistoricalResponse
from ..models.team_token_usage_response import TeamTokenUsageResponse
from ..server.server import Server


class Billing:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BillingWithRawResponse(client, server, auth)

    def get_credit_usage(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamCreditUsageResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Credit usage information not found Server error ``error`` is ``TeamCreditUsage404Error1 |
                TeamCreditUsage500Error1 | RawError``."""
        return self._with_raw_response.get_credit_usage(request_options=request_options).unwrap()

    def get_historical_credit_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> TeamCreditUsageHistoricalResponse:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical credit usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Server error ``error`` is ``TeamCreditUsageHistorical500Error1 | RawError``."""
        return self._with_raw_response.get_historical_credit_usage(
            by_api_key=by_api_key, request_options=request_options
        ).unwrap()

    def get_historical_token_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTokenUsageHistoricalResponse:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical token usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Server error ``error`` is ``TeamTokenUsageHistorical500Error1 | RawError``."""
        return self._with_raw_response.get_historical_token_usage(
            by_api_key=by_api_key, request_options=request_options
        ).unwrap()

    def get_token_usage(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamTokenUsageResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Token usage information not found Server error ``error`` is ``TeamTokenUsage404Error1 |
                TeamTokenUsage500Error1 | RawError``."""
        return self._with_raw_response.get_token_usage(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BillingWithRawResponse:
        return self._with_raw_response


class AsyncBilling:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBillingWithRawResponse(client, server, auth)

    async def get_credit_usage(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamCreditUsageResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Credit usage information not found Server error ``error`` is ``TeamCreditUsage404Error1 |
                TeamCreditUsage500Error1 | RawError``."""
        return (await self._with_raw_response.get_credit_usage(request_options=request_options)).unwrap()

    async def get_historical_credit_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> TeamCreditUsageHistoricalResponse:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical credit usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Server error ``error`` is ``TeamCreditUsageHistorical500Error1 | RawError``."""
        return (
            await self._with_raw_response.get_historical_credit_usage(
                by_api_key=by_api_key, request_options=request_options
            )
        ).unwrap()

    async def get_historical_token_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTokenUsageHistoricalResponse:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical token usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Server error ``error`` is ``TeamTokenUsageHistorical500Error1 | RawError``."""
        return (
            await self._with_raw_response.get_historical_token_usage(
                by_api_key=by_api_key, request_options=request_options
            )
        ).unwrap()

    async def get_token_usage(self, *, request_options: RequestOptionsOrDict | None = None) -> TeamTokenUsageResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Token usage information not found Server error ``error`` is ``TeamTokenUsage404Error1 |
                TeamTokenUsage500Error1 | RawError``."""
        return (await self._with_raw_response.get_token_usage(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncBillingWithRawResponse:
        return self._with_raw_response


class BillingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_credit_usage(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamCreditUsageResponse, GetCreditUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/credit-usage"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamCreditUsageResponse],
            error_mapper=get_credit_usage_error_mapper,
            request_options=request_options,
        )

    def get_historical_credit_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamCreditUsageHistoricalResponse, GetHistoricalCreditUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical credit usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/credit-usage/historical"),
            query_params=[param[bool | None]("byApiKey", by_api_key)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamCreditUsageHistoricalResponse],
            error_mapper=get_historical_credit_usage_error_mapper,
            request_options=request_options,
        )

    def get_historical_token_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTokenUsageHistoricalResponse, GetHistoricalTokenUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical token usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/token-usage/historical"),
            query_params=[param[bool | None]("byApiKey", by_api_key)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamTokenUsageHistoricalResponse],
            error_mapper=get_historical_token_usage_error_mapper,
            request_options=request_options,
        )

    def get_token_usage(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTokenUsageResponse, GetTokenUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/token-usage"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamTokenUsageResponse],
            error_mapper=get_token_usage_error_mapper,
            request_options=request_options,
        )


class AsyncBillingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_credit_usage(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamCreditUsageResponse, GetCreditUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/credit-usage"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamCreditUsageResponse],
            error_mapper=get_credit_usage_error_mapper,
            request_options=request_options,
        )

    async def get_historical_credit_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamCreditUsageHistoricalResponse, GetHistoricalCreditUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical credit usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/credit-usage/historical"),
            query_params=[param[bool | None]("byApiKey", by_api_key)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamCreditUsageHistoricalResponse],
            error_mapper=get_historical_credit_usage_error_mapper,
            request_options=request_options,
        )

    async def get_historical_token_usage(
        self, *, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTokenUsageHistoricalResponse, GetHistoricalTokenUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            by_api_key: Get historical token usage by API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/token-usage/historical"),
            query_params=[param[bool | None]("byApiKey", by_api_key)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamTokenUsageHistoricalResponse],
            error_mapper=get_historical_token_usage_error_mapper,
            request_options=request_options,
        )

    async def get_token_usage(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTokenUsageResponse, GetTokenUsageErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/team/token-usage"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TeamTokenUsageResponse],
            error_mapper=get_token_usage_error_mapper,
            request_options=request_options,
        )
