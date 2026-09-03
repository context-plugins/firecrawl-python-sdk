from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.start_agent_error import StartAgentErrorBody, start_agent_error_mapper
from ..models.agent_request import AgentRequest, AgentRequestDict
from ..models.agent_response import AgentResponse
from ..models.agent_response1 import AgentResponse1
from ..models.success_response import SuccessResponse
from ..server.server import Server


class Agent:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AgentWithRawResponse(client, server, auth)

    def cancel_agent(self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> SuccessResponse:
        """Send a ``DELETE`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent job cancelled successfully

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_agent(job_id, request_options=request_options).unwrap()

    def get_agent_status(self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> AgentResponse1:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_agent_status(job_id, request_options=request_options).unwrap()

    def start_agent(
        self, body: AgentRequest | AgentRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent task started successfully

        Raises:
            ApiError: Payment required Too many requests ``error`` is ``Agent402Error1 | Agent429Error1 | RawError``."""
        return self._with_raw_response.start_agent(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AgentWithRawResponse:
        return self._with_raw_response


class AsyncAgent:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAgentWithRawResponse(client, server, auth)

    async def cancel_agent(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Send a ``DELETE`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent job cancelled successfully

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.cancel_agent(job_id, request_options=request_options)).unwrap()

    async def get_agent_status(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentResponse1:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_agent_status(job_id, request_options=request_options)).unwrap()

    async def start_agent(
        self, body: AgentRequest | AgentRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent task started successfully

        Raises:
            ApiError: Payment required Too many requests ``error`` is ``Agent402Error1 | Agent429Error1 | RawError``."""
        return (await self._with_raw_response.start_agent(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAgentWithRawResponse:
        return self._with_raw_response


class AgentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_agent(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, RawError]:
        """Send a ``DELETE`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/agent/{jobId}"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SuccessResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_agent_status(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentResponse1, RawError]:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/agent/{jobId}"),
            path_params=[param[UUID]("jobId", job_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[AgentResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def start_agent(
        self, body: AgentRequest | AgentRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentResponse, StartAgentErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/agent"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AgentRequest | AgentRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[AgentResponse],
            error_mapper=start_agent_error_mapper,
            request_options=request_options,
        )


class AsyncAgentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_agent(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, RawError]:
        """Send a ``DELETE`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/agent/{jobId}"),
            path_params=[param[UUID]("jobId", job_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SuccessResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_agent_status(
        self, job_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentResponse1, RawError]:
        """Send a ``GET`` request.

        Args:
            job_id: The ID of the agent job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/agent/{jobId}"),
            path_params=[param[UUID]("jobId", job_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[AgentResponse1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def start_agent(
        self, body: AgentRequest | AgentRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentResponse, StartAgentErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/agent"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AgentRequest | AgentRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[AgentResponse],
            error_mapper=start_agent_error_mapper,
            request_options=request_options,
        )
