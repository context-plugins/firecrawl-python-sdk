from __future__ import annotations

from uuid import UUID

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.cancel_crawl_error import CancelCrawlErrorBody, cancel_crawl_error_mapper
from ..errors.crawl_params_preview_error import CrawlParamsPreviewErrorBody, crawl_params_preview_error_mapper
from ..errors.crawl_urls_error import CrawlUrlsErrorBody, crawl_urls_error_mapper
from ..errors.get_active_crawls_error import GetActiveCrawlsErrorBody, get_active_crawls_error_mapper
from ..errors.get_crawl_errors_error import GetCrawlErrorsErrorBody, get_crawl_errors_error_mapper
from ..errors.get_crawl_status_error import GetCrawlStatusErrorBody, get_crawl_status_error_mapper
from ..models.crawl_active_response import CrawlActiveResponse
from ..models.crawl_errors_response_obj import CrawlErrorsResponseObj
from ..models.crawl_params_preview_request import CrawlParamsPreviewRequest, CrawlParamsPreviewRequestDict
from ..models.crawl_params_preview_response import CrawlParamsPreviewResponse
from ..models.crawl_request import CrawlRequest, CrawlRequestDict
from ..models.crawl_response import CrawlResponse
from ..models.crawl_response1 import CrawlResponse1
from ..models.crawl_status_response_obj import CrawlStatusResponseObj
from ..server.server import Server


class Crawling:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CrawlingWithRawResponse(client, server, auth)

    def cancel_crawl(self, id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> CrawlResponse1:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful cancellation

        Raises:
            ApiError: Crawl job not found Server error ``error`` is ``Crawl404Error1 | Crawl500Error1 | RawError``."""
        return self._with_raw_response.cancel_crawl(id, request_options=request_options).unwrap()

    def crawl_params_preview(
        self,
        body: CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CrawlParamsPreviewResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response with generated crawl parameters

        Raises:
            ApiError: Bad request Unauthorized Server error ``error`` is ``CrawlParamsPreview400Error1 |
                CrawlParamsPreview401Error1 | CrawlParamsPreview500Error1 | RawError``."""
        return self._with_raw_response.crawl_params_preview(body, request_options=request_options).unwrap()

    def crawl_urls(
        self, body: CrawlRequest | CrawlRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Crawl402Error1 | Crawl429Error1 |
                Crawl500Error1 | RawError``."""
        return self._with_raw_response.crawl_urls(body, request_options=request_options).unwrap()

    def get_active_crawls(self, *, request_options: RequestOptionsOrDict | None = None) -> CrawlActiveResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``CrawlActive402Error1 |
                CrawlActive429Error1 | CrawlActive500Error1 | RawError``."""
        return self._with_raw_response.get_active_crawls(request_options=request_options).unwrap()

    def get_crawl_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlErrorsResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``CrawlErrors402Error1 |
                CrawlErrors429Error1 | CrawlErrors500Error1 | RawError``."""
        return self._with_raw_response.get_crawl_errors(id, request_options=request_options).unwrap()

    def get_crawl_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlStatusResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Crawl402Error1 | Crawl429Error1 |
                Crawl500Error1 | RawError``."""
        return self._with_raw_response.get_crawl_status(id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CrawlingWithRawResponse:
        return self._with_raw_response


class AsyncCrawling:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCrawlingWithRawResponse(client, server, auth)

    async def cancel_crawl(self, id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> CrawlResponse1:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful cancellation

        Raises:
            ApiError: Crawl job not found Server error ``error`` is ``Crawl404Error1 | Crawl500Error1 | RawError``."""
        return (await self._with_raw_response.cancel_crawl(id, request_options=request_options)).unwrap()

    async def crawl_params_preview(
        self,
        body: CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CrawlParamsPreviewResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response with generated crawl parameters

        Raises:
            ApiError: Bad request Unauthorized Server error ``error`` is ``CrawlParamsPreview400Error1 |
                CrawlParamsPreview401Error1 | CrawlParamsPreview500Error1 | RawError``."""
        return (await self._with_raw_response.crawl_params_preview(body, request_options=request_options)).unwrap()

    async def crawl_urls(
        self, body: CrawlRequest | CrawlRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Crawl402Error1 | Crawl429Error1 |
                Crawl500Error1 | RawError``."""
        return (await self._with_raw_response.crawl_urls(body, request_options=request_options)).unwrap()

    async def get_active_crawls(self, *, request_options: RequestOptionsOrDict | None = None) -> CrawlActiveResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``CrawlActive402Error1 |
                CrawlActive429Error1 | CrawlActive500Error1 | RawError``."""
        return (await self._with_raw_response.get_active_crawls(request_options=request_options)).unwrap()

    async def get_crawl_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlErrorsResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``CrawlErrors402Error1 |
                CrawlErrors429Error1 | CrawlErrors500Error1 | RawError``."""
        return (await self._with_raw_response.get_crawl_errors(id, request_options=request_options)).unwrap()

    async def get_crawl_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlStatusResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Crawl402Error1 | Crawl429Error1 |
                Crawl500Error1 | RawError``."""
        return (await self._with_raw_response.get_crawl_status(id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCrawlingWithRawResponse:
        return self._with_raw_response


class CrawlingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_crawl(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlResponse1, CancelCrawlErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/crawl/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlResponse1],
            error_mapper=cancel_crawl_error_mapper,
            request_options=request_options,
        )

    def crawl_params_preview(
        self,
        body: CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CrawlParamsPreviewResponse, CrawlParamsPreviewErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/crawl/params-preview"),
            body=json_body[CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlParamsPreviewResponse],
            error_mapper=crawl_params_preview_error_mapper,
            request_options=request_options,
        )

    def crawl_urls(
        self, body: CrawlRequest | CrawlRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlResponse, CrawlUrlsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/crawl"),
            body=json_body[CrawlRequest | CrawlRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlResponse],
            error_mapper=crawl_urls_error_mapper,
            request_options=request_options,
        )

    def get_active_crawls(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlActiveResponse, GetActiveCrawlsErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crawl/active"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlActiveResponse],
            error_mapper=get_active_crawls_error_mapper,
            request_options=request_options,
        )

    def get_crawl_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlErrorsResponseObj, GetCrawlErrorsErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crawl/{id}/errors"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlErrorsResponseObj],
            error_mapper=get_crawl_errors_error_mapper,
            request_options=request_options,
        )

    def get_crawl_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlStatusResponseObj, GetCrawlStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crawl/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlStatusResponseObj],
            error_mapper=get_crawl_status_error_mapper,
            request_options=request_options,
        )


class AsyncCrawlingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_crawl(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlResponse1, CancelCrawlErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/crawl/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlResponse1],
            error_mapper=cancel_crawl_error_mapper,
            request_options=request_options,
        )

    async def crawl_params_preview(
        self,
        body: CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CrawlParamsPreviewResponse, CrawlParamsPreviewErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/crawl/params-preview"),
            body=json_body[CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlParamsPreviewResponse],
            error_mapper=crawl_params_preview_error_mapper,
            request_options=request_options,
        )

    async def crawl_urls(
        self, body: CrawlRequest | CrawlRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlResponse, CrawlUrlsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/crawl"),
            body=json_body[CrawlRequest | CrawlRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlResponse],
            error_mapper=crawl_urls_error_mapper,
            request_options=request_options,
        )

    async def get_active_crawls(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlActiveResponse, GetActiveCrawlsErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crawl/active"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlActiveResponse],
            error_mapper=get_active_crawls_error_mapper,
            request_options=request_options,
        )

    async def get_crawl_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlErrorsResponseObj, GetCrawlErrorsErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crawl/{id}/errors"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlErrorsResponseObj],
            error_mapper=get_crawl_errors_error_mapper,
            request_options=request_options,
        )

    async def get_crawl_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlStatusResponseObj, GetCrawlStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the crawl job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/crawl/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlStatusResponseObj],
            error_mapper=get_crawl_status_error_mapper,
            request_options=request_options,
        )
