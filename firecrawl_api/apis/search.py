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
    param,
)
from ..errors.search_and_scrape_error import SearchAndScrapeErrorBody, search_and_scrape_error_mapper
from ..errors.submit_search_feedback_error import SubmitSearchFeedbackErrorBody, submit_search_feedback_error_mapper
from ..models.feedback_response import FeedbackResponse
from ..models.search_feedback_request import SearchFeedbackRequest, SearchFeedbackRequestDict
from ..models.search_request import SearchRequest, SearchRequestDict
from ..models.search_response import SearchResponse
from ..server.server import Server


class Search:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchWithRawResponse(client, server, auth)

    def search_and_scrape(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> SearchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Request timeout Server error ``error`` is ``Search408Error1 | Search500Error1 | RawError``."""
        return self._with_raw_response.search_and_scrape(body, request_options=request_options).unwrap()

    def submit_search_feedback(
        self,
        job_id: UUID,
        body: SearchFeedbackRequest | SearchFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedbackResponse:
        """Send a ``POST`` request.

        Args:
            job_id: Search job id returned by /search.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Feedback recorded

        Raises:
            ApiError: Invalid request body Feedback is not available for this team Search not found for this team
                Feedback cannot be recorded for this search Server error ``error`` is ``FeedbackErrorResponse |
                RawError``."""
        return self._with_raw_response.submit_search_feedback(job_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SearchWithRawResponse:
        return self._with_raw_response


class AsyncSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchWithRawResponse(client, server, auth)

    async def search_and_scrape(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> SearchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: Request timeout Server error ``error`` is ``Search408Error1 | Search500Error1 | RawError``."""
        return (await self._with_raw_response.search_and_scrape(body, request_options=request_options)).unwrap()

    async def submit_search_feedback(
        self,
        job_id: UUID,
        body: SearchFeedbackRequest | SearchFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedbackResponse:
        """Send a ``POST`` request.

        Args:
            job_id: Search job id returned by /search.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Feedback recorded

        Raises:
            ApiError: Invalid request body Feedback is not available for this team Search not found for this team
                Feedback cannot be recorded for this search Server error ``error`` is ``FeedbackErrorResponse |
                RawError``."""
        return (
            await self._with_raw_response.submit_search_feedback(job_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSearchWithRawResponse:
        return self._with_raw_response


class SearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search_and_scrape(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchResponse, SearchAndScrapeErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchRequest | SearchRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SearchResponse],
            error_mapper=search_and_scrape_error_mapper,
            request_options=request_options,
        )

    def submit_search_feedback(
        self,
        job_id: UUID,
        body: SearchFeedbackRequest | SearchFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedbackResponse, SubmitSearchFeedbackErrorBody]:
        """Send a ``POST`` request.

        Args:
            job_id: Search job id returned by /search.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/search/{jobId}/feedback"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchFeedbackRequest | SearchFeedbackRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FeedbackResponse],
            error_mapper=submit_search_feedback_error_mapper,
            request_options=request_options,
        )


class AsyncSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search_and_scrape(
        self, body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SearchResponse, SearchAndScrapeErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchRequest | SearchRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SearchResponse],
            error_mapper=search_and_scrape_error_mapper,
            request_options=request_options,
        )

    async def submit_search_feedback(
        self,
        job_id: UUID,
        body: SearchFeedbackRequest | SearchFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedbackResponse, SubmitSearchFeedbackErrorBody]:
        """Send a ``POST`` request.

        Args:
            job_id: Search job id returned by /search.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/search/{jobId}/feedback"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchFeedbackRequest | SearchFeedbackRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FeedbackResponse],
            error_mapper=submit_search_feedback_error_mapper,
            request_options=request_options,
        )
