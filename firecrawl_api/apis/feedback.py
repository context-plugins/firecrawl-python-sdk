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
from ..errors.submit_endpoint_feedback_error import (
    SubmitEndpointFeedbackErrorBody,
    submit_endpoint_feedback_error_mapper,
)
from ..errors.submit_search_feedback_error import SubmitSearchFeedbackErrorBody, submit_search_feedback_error_mapper
from ..models.endpoint_feedback_request import EndpointFeedbackRequest, EndpointFeedbackRequestDict
from ..models.feedback_response import FeedbackResponse
from ..models.search_feedback_request import SearchFeedbackRequest, SearchFeedbackRequestDict
from ..server.server import Server


class Feedback:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FeedbackWithRawResponse(client, server, auth)

    def submit_endpoint_feedback(
        self,
        body: EndpointFeedbackRequest | EndpointFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedbackResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Feedback recorded

        Raises:
            ApiError: Invalid request body Feedback is not available for this team Job not found for this team Feedback
                cannot be recorded for this job Server error ``error`` is ``FeedbackErrorResponse | RawError``."""
        return self._with_raw_response.submit_endpoint_feedback(body, request_options=request_options).unwrap()

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
    def with_raw_response(self) -> FeedbackWithRawResponse:
        return self._with_raw_response


class AsyncFeedback:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFeedbackWithRawResponse(client, server, auth)

    async def submit_endpoint_feedback(
        self,
        body: EndpointFeedbackRequest | EndpointFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedbackResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Feedback recorded

        Raises:
            ApiError: Invalid request body Feedback is not available for this team Job not found for this team Feedback
                cannot be recorded for this job Server error ``error`` is ``FeedbackErrorResponse | RawError``."""
        return (await self._with_raw_response.submit_endpoint_feedback(body, request_options=request_options)).unwrap()

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
    def with_raw_response(self) -> AsyncFeedbackWithRawResponse:
        return self._with_raw_response


class FeedbackWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def submit_endpoint_feedback(
        self,
        body: EndpointFeedbackRequest | EndpointFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedbackResponse, SubmitEndpointFeedbackErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/feedback"),
            body=json_body[EndpointFeedbackRequest | EndpointFeedbackRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FeedbackResponse],
            error_mapper=submit_endpoint_feedback_error_mapper,
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
            body=json_body[SearchFeedbackRequest | SearchFeedbackRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FeedbackResponse],
            error_mapper=submit_search_feedback_error_mapper,
            request_options=request_options,
        )


class AsyncFeedbackWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def submit_endpoint_feedback(
        self,
        body: EndpointFeedbackRequest | EndpointFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedbackResponse, SubmitEndpointFeedbackErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/feedback"),
            body=json_body[EndpointFeedbackRequest | EndpointFeedbackRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FeedbackResponse],
            error_mapper=submit_endpoint_feedback_error_mapper,
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
            body=json_body[SearchFeedbackRequest | SearchFeedbackRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FeedbackResponse],
            error_mapper=submit_search_feedback_error_mapper,
            request_options=request_options,
        )
