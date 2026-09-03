from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    multipart_body,
    param,
)
from ..errors.cancel_batch_scrape_error import CancelBatchScrapeErrorBody, cancel_batch_scrape_error_mapper
from ..errors.get_batch_scrape_errors_error import GetBatchScrapeErrorsErrorBody, get_batch_scrape_errors_error_mapper
from ..errors.get_batch_scrape_status_error import GetBatchScrapeStatusErrorBody, get_batch_scrape_status_error_mapper
from ..errors.get_scrape_status_error import GetScrapeStatusErrorBody, get_scrape_status_error_mapper
from ..errors.interact_with_scrape_browser_session_error import (
    InteractWithScrapeBrowserSessionErrorBody,
    interact_with_scrape_browser_session_error_mapper,
)
from ..errors.parse_file_error import ParseFileErrorBody, parse_file_error_mapper
from ..errors.scrape_and_extract_from_url_error import (
    ScrapeAndExtractFromUrlErrorBody,
    scrape_and_extract_from_url_error_mapper,
)
from ..errors.scrape_and_extract_from_urls_error import (
    ScrapeAndExtractFromUrlsErrorBody,
    scrape_and_extract_from_urls_error_mapper,
)
from ..errors.stop_interactive_scrape_browser_session_error import (
    StopInteractiveScrapeBrowserSessionErrorBody,
    stop_interactive_scrape_browser_session_error_mapper,
)
from ..models.batch_scrape_request import BatchScrapeRequest, BatchScrapeRequestDict
from ..models.batch_scrape_response import BatchScrapeResponse
from ..models.batch_scrape_response_obj import BatchScrapeResponseObj
from ..models.batch_scrape_status_response_obj import BatchScrapeStatusResponseObj
from ..models.crawl_errors_response_obj import CrawlErrorsResponseObj
from ..models.parse_options import ParseOptions, ParseOptionsDict
from ..models.scrape_interact_request import ScrapeInteractRequest, ScrapeInteractRequestDict
from ..models.scrape_interact_response import ScrapeInteractResponse
from ..models.scrape_request import ScrapeRequest, ScrapeRequestDict
from ..models.scrape_response import ScrapeResponse
from ..models.success_response import SuccessResponse
from ..server.server import Server


class Scraping:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ScrapingWithRawResponse(client, server, auth)

    def cancel_batch_scrape(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchScrapeResponse:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful cancellation

        Raises:
            ApiError: Batch scrape job not found Server error ``error`` is ``BatchScrape404Error1 | BatchScrape500Error1
                | RawError``."""
        return self._with_raw_response.cancel_batch_scrape(id, request_options=request_options).unwrap()

    def get_batch_scrape_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlErrorsResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``BatchScrapeErrors402Error1 |
                BatchScrapeErrors429Error1 | BatchScrapeErrors500Error1 | RawError``."""
        return self._with_raw_response.get_batch_scrape_errors(id, request_options=request_options).unwrap()

    def get_batch_scrape_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchScrapeStatusResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``BatchScrape402Error1 |
                BatchScrape429Error1 | BatchScrape500Error1 | RawError``."""
        return self._with_raw_response.get_batch_scrape_status(id, request_options=request_options).unwrap()

    def get_scrape_status(self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ScrapeResponse:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Scrape job status

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Scrape402Error21 | Scrape429Error21
                | Scrape500Error21 | RawError``."""
        return self._with_raw_response.get_scrape_status(job_id, request_options=request_options).unwrap()

    def interact_with_scrape_browser_session(
        self,
        job_id: UUID,
        body: ScrapeInteractRequest | ScrapeInteractRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScrapeInteractResponse:
        """Send a ``POST`` request.

        Args:
            job_id: The scrape job ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code executed successfully

        Raises:
            ApiError: Invalid job ID Payment required Forbidden Scrape job not found Scrape replay context is
                unavailable or session could not be initialized Scrape browser session has already been destroyed Too
                many active browser sessions Failed to communicate with browser service ``error`` is
                ``ScrapeInteract400Error1 | ScrapeInteract402Error1 | ScrapeInteract403Error1 | ScrapeInteract404Error1
                | ScrapeInteract409Error1 | ScrapeInteract410Error1 | ScrapeInteract429Error1 | ScrapeInteract502Error1
                | RawError``."""
        return self._with_raw_response.interact_with_scrape_browser_session(
            job_id, body, request_options=request_options
        ).unwrap()

    def parse_file(
        self,
        file: bytes,
        *,
        options: ParseOptions | ParseOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScrapeResponse:
        """Send a ``POST`` request.

        Args:
            file: The file bytes to parse. Supported extensions: .html, .htm, .xhtml, .pdf, .docx, .doc, .docm, .odt,
                .ods, .odp, .rtf, .xlsx, .xls, .xlsm, .xlsb, .pptx, .ppt, .pptm, .epub, .csv.
            options: Optional parse options sent as JSON in the multipart ``options`` field.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Bad request Payment required Too many requests Server error ``error`` is ``Parse400Error1 |
                Parse402Error1 | Parse429Error1 | Parse500Error1 | RawError``."""
        return self._with_raw_response.parse_file(file, options=options, request_options=request_options).unwrap()

    def scrape_and_extract_from_url(
        self, body: ScrapeRequest | ScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScrapeResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Scrape402Error1 | Scrape429Error1 |
                Scrape500Error1 | RawError``."""
        return self._with_raw_response.scrape_and_extract_from_url(body, request_options=request_options).unwrap()

    def scrape_and_extract_from_urls(
        self, body: BatchScrapeRequest | BatchScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchScrapeResponseObj:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``BatchScrape402Error1 |
                BatchScrape429Error1 | BatchScrape500Error1 | RawError``."""
        return self._with_raw_response.scrape_and_extract_from_urls(body, request_options=request_options).unwrap()

    def stop_interactive_scrape_browser_session(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Send a ``DELETE`` request.

        Args:
            job_id: The scrape job ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interactive scrape browser session stopped successfully

        Raises:
            ApiError: Forbidden Interactive scrape browser session not found ``error`` is ``ScrapeInteract403Error1 |
                ScrapeInteract404Error1 | RawError``."""
        return self._with_raw_response.stop_interactive_scrape_browser_session(
            job_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ScrapingWithRawResponse:
        return self._with_raw_response


class AsyncScraping:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncScrapingWithRawResponse(client, server, auth)

    async def cancel_batch_scrape(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchScrapeResponse:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful cancellation

        Raises:
            ApiError: Batch scrape job not found Server error ``error`` is ``BatchScrape404Error1 | BatchScrape500Error1
                | RawError``."""
        return (await self._with_raw_response.cancel_batch_scrape(id, request_options=request_options)).unwrap()

    async def get_batch_scrape_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> CrawlErrorsResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``BatchScrapeErrors402Error1 |
                BatchScrapeErrors429Error1 | BatchScrapeErrors500Error1 | RawError``."""
        return (await self._with_raw_response.get_batch_scrape_errors(id, request_options=request_options)).unwrap()

    async def get_batch_scrape_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchScrapeStatusResponseObj:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``BatchScrape402Error1 |
                BatchScrape429Error1 | BatchScrape500Error1 | RawError``."""
        return (await self._with_raw_response.get_batch_scrape_status(id, request_options=request_options)).unwrap()

    async def get_scrape_status(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScrapeResponse:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Scrape job status

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Scrape402Error21 | Scrape429Error21
                | Scrape500Error21 | RawError``."""
        return (await self._with_raw_response.get_scrape_status(job_id, request_options=request_options)).unwrap()

    async def interact_with_scrape_browser_session(
        self,
        job_id: UUID,
        body: ScrapeInteractRequest | ScrapeInteractRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScrapeInteractResponse:
        """Send a ``POST`` request.

        Args:
            job_id: The scrape job ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code executed successfully

        Raises:
            ApiError: Invalid job ID Payment required Forbidden Scrape job not found Scrape replay context is
                unavailable or session could not be initialized Scrape browser session has already been destroyed Too
                many active browser sessions Failed to communicate with browser service ``error`` is
                ``ScrapeInteract400Error1 | ScrapeInteract402Error1 | ScrapeInteract403Error1 | ScrapeInteract404Error1
                | ScrapeInteract409Error1 | ScrapeInteract410Error1 | ScrapeInteract429Error1 | ScrapeInteract502Error1
                | RawError``."""
        return (
            await self._with_raw_response.interact_with_scrape_browser_session(
                job_id, body, request_options=request_options
            )
        ).unwrap()

    async def parse_file(
        self,
        file: bytes,
        *,
        options: ParseOptions | ParseOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScrapeResponse:
        """Send a ``POST`` request.

        Args:
            file: The file bytes to parse. Supported extensions: .html, .htm, .xhtml, .pdf, .docx, .doc, .docm, .odt,
                .ods, .odp, .rtf, .xlsx, .xls, .xlsm, .xlsb, .pptx, .ppt, .pptm, .epub, .csv.
            options: Optional parse options sent as JSON in the multipart ``options`` field.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Bad request Payment required Too many requests Server error ``error`` is ``Parse400Error1 |
                Parse402Error1 | Parse429Error1 | Parse500Error1 | RawError``."""
        return (
            await self._with_raw_response.parse_file(file, options=options, request_options=request_options)
        ).unwrap()

    async def scrape_and_extract_from_url(
        self, body: ScrapeRequest | ScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ScrapeResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``Scrape402Error1 | Scrape429Error1 |
                Scrape500Error1 | RawError``."""
        return (
            await self._with_raw_response.scrape_and_extract_from_url(body, request_options=request_options)
        ).unwrap()

    async def scrape_and_extract_from_urls(
        self, body: BatchScrapeRequest | BatchScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> BatchScrapeResponseObj:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Payment required Too many requests Server error ``error`` is ``BatchScrape402Error1 |
                BatchScrape429Error1 | BatchScrape500Error1 | RawError``."""
        return (
            await self._with_raw_response.scrape_and_extract_from_urls(body, request_options=request_options)
        ).unwrap()

    async def stop_interactive_scrape_browser_session(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Send a ``DELETE`` request.

        Args:
            job_id: The scrape job ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interactive scrape browser session stopped successfully

        Raises:
            ApiError: Forbidden Interactive scrape browser session not found ``error`` is ``ScrapeInteract403Error1 |
                ScrapeInteract404Error1 | RawError``."""
        return (
            await self._with_raw_response.stop_interactive_scrape_browser_session(
                job_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncScrapingWithRawResponse:
        return self._with_raw_response


class ScrapingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_batch_scrape(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchScrapeResponse, CancelBatchScrapeErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/batch/scrape/{id}"),
            path_params=[param[UUID]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[BatchScrapeResponse],
            error_mapper=cancel_batch_scrape_error_mapper,
            request_options=request_options,
        )

    def get_batch_scrape_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlErrorsResponseObj, GetBatchScrapeErrorsErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/batch/scrape/{id}/errors"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlErrorsResponseObj],
            error_mapper=get_batch_scrape_errors_error_mapper,
            request_options=request_options,
        )

    def get_batch_scrape_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchScrapeStatusResponseObj, GetBatchScrapeStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/batch/scrape/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[BatchScrapeStatusResponseObj],
            error_mapper=get_batch_scrape_status_error_mapper,
            request_options=request_options,
        )

    def get_scrape_status(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScrapeResponse, GetScrapeStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scrape/{jobId}"),
            path_params=[param[UUID]("jobId", job_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeResponse],
            error_mapper=get_scrape_status_error_mapper,
            request_options=request_options,
        )

    def interact_with_scrape_browser_session(
        self,
        job_id: UUID,
        body: ScrapeInteractRequest | ScrapeInteractRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScrapeInteractResponse, InteractWithScrapeBrowserSessionErrorBody]:
        """Send a ``POST`` request.

        Args:
            job_id: The scrape job ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/scrape/{jobId}/interact"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScrapeInteractRequest | ScrapeInteractRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeInteractResponse],
            error_mapper=interact_with_scrape_browser_session_error_mapper,
            request_options=request_options,
        )

    def parse_file(
        self,
        file: bytes,
        *,
        options: ParseOptions | ParseOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScrapeResponse, ParseFileErrorBody]:
        """Send a ``POST`` request.

        Args:
            file: The file bytes to parse. Supported extensions: .html, .htm, .xhtml, .pdf, .docx, .doc, .docm, .odt,
                .ods, .odp, .rtf, .xlsx, .xls, .xlsm, .xlsb, .pptx, .ppt, .pptm, .epub, .csv.
            options: Optional parse options sent as JSON in the multipart ``options`` field.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/parse"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body([param[ParseOptions | ParseOptionsDict | None]("options", options)], {"file": file}),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeResponse],
            error_mapper=parse_file_error_mapper,
            request_options=request_options,
        )

    def scrape_and_extract_from_url(
        self, body: ScrapeRequest | ScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScrapeResponse, ScrapeAndExtractFromUrlErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/scrape"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScrapeRequest | ScrapeRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeResponse],
            error_mapper=scrape_and_extract_from_url_error_mapper,
            request_options=request_options,
        )

    def scrape_and_extract_from_urls(
        self, body: BatchScrapeRequest | BatchScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchScrapeResponseObj, ScrapeAndExtractFromUrlsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/batch/scrape"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchScrapeRequest | BatchScrapeRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[BatchScrapeResponseObj],
            error_mapper=scrape_and_extract_from_urls_error_mapper,
            request_options=request_options,
        )

    def stop_interactive_scrape_browser_session(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, StopInteractiveScrapeBrowserSessionErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            job_id: The scrape job ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/scrape/{jobId}/interact"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SuccessResponse],
            error_mapper=stop_interactive_scrape_browser_session_error_mapper,
            request_options=request_options,
        )


class AsyncScrapingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_batch_scrape(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchScrapeResponse, CancelBatchScrapeErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/batch/scrape/{id}"),
            path_params=[param[UUID]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[BatchScrapeResponse],
            error_mapper=cancel_batch_scrape_error_mapper,
            request_options=request_options,
        )

    async def get_batch_scrape_errors(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CrawlErrorsResponseObj, GetBatchScrapeErrorsErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/batch/scrape/{id}/errors"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CrawlErrorsResponseObj],
            error_mapper=get_batch_scrape_errors_error_mapper,
            request_options=request_options,
        )

    async def get_batch_scrape_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchScrapeStatusResponseObj, GetBatchScrapeStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the batch scrape job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/batch/scrape/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[BatchScrapeStatusResponseObj],
            error_mapper=get_batch_scrape_status_error_mapper,
            request_options=request_options,
        )

    async def get_scrape_status(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScrapeResponse, GetScrapeStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/scrape/{jobId}"),
            path_params=[param[UUID]("jobId", job_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeResponse],
            error_mapper=get_scrape_status_error_mapper,
            request_options=request_options,
        )

    async def interact_with_scrape_browser_session(
        self,
        job_id: UUID,
        body: ScrapeInteractRequest | ScrapeInteractRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScrapeInteractResponse, InteractWithScrapeBrowserSessionErrorBody]:
        """Send a ``POST`` request.

        Args:
            job_id: The scrape job ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/scrape/{jobId}/interact"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScrapeInteractRequest | ScrapeInteractRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeInteractResponse],
            error_mapper=interact_with_scrape_browser_session_error_mapper,
            request_options=request_options,
        )

    async def parse_file(
        self,
        file: bytes,
        *,
        options: ParseOptions | ParseOptionsDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScrapeResponse, ParseFileErrorBody]:
        """Send a ``POST`` request.

        Args:
            file: The file bytes to parse. Supported extensions: .html, .htm, .xhtml, .pdf, .docx, .doc, .docm, .odt,
                .ods, .odp, .rtf, .xlsx, .xls, .xlsm, .xlsb, .pptx, .ppt, .pptm, .epub, .csv.
            options: Optional parse options sent as JSON in the multipart ``options`` field.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/parse"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body([param[ParseOptions | ParseOptionsDict | None]("options", options)], {"file": file}),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeResponse],
            error_mapper=parse_file_error_mapper,
            request_options=request_options,
        )

    async def scrape_and_extract_from_url(
        self, body: ScrapeRequest | ScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ScrapeResponse, ScrapeAndExtractFromUrlErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/scrape"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScrapeRequest | ScrapeRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ScrapeResponse],
            error_mapper=scrape_and_extract_from_url_error_mapper,
            request_options=request_options,
        )

    async def scrape_and_extract_from_urls(
        self, body: BatchScrapeRequest | BatchScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BatchScrapeResponseObj, ScrapeAndExtractFromUrlsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/batch/scrape"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchScrapeRequest | BatchScrapeRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[BatchScrapeResponseObj],
            error_mapper=scrape_and_extract_from_urls_error_mapper,
            request_options=request_options,
        )

    async def stop_interactive_scrape_browser_session(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, StopInteractiveScrapeBrowserSessionErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            job_id: The scrape job ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/scrape/{jobId}/interact"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SuccessResponse],
            error_mapper=stop_interactive_scrape_browser_session_error_mapper,
            request_options=request_options,
        )
