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
from ..errors.create_browser_session_error import CreateBrowserSessionErrorBody, create_browser_session_error_mapper
from ..errors.delete_browser_session_error import DeleteBrowserSessionErrorBody, delete_browser_session_error_mapper
from ..errors.execute_browser_code_error import ExecuteBrowserCodeErrorBody, execute_browser_code_error_mapper
from ..errors.list_browser_sessions_error import ListBrowserSessionsErrorBody, list_browser_sessions_error_mapper
from ..models.enums.status10 import Status10OrStr
from ..models.interact_execute_request import InteractExecuteRequest, InteractExecuteRequestDict
from ..models.interact_execute_response import InteractExecuteResponse
from ..models.interact_request import InteractRequest, InteractRequestDict
from ..models.interact_response import InteractResponse
from ..models.interact_response1 import InteractResponse1
from ..models.interact_response2 import InteractResponse2
from ..server.server import Server


class Interact:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InteractWithRawResponse(client, server, auth)

    def create_browser_session(
        self, body: InteractRequest | InteractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> InteractResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interact session created successfully

        Raises:
            ApiError: Payment required ``error`` is ``Interact402Error1 | RawError``."""
        return self._with_raw_response.create_browser_session(body, request_options=request_options).unwrap()

    def delete_browser_session(
        self, session_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InteractResponse2:
        """Send a ``DELETE`` request.

        Args:
            session_id: The interact session ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interact session deleted successfully

        Raises:
            ApiError: Payment required ``error`` is ``Interact402Error1 | RawError``."""
        return self._with_raw_response.delete_browser_session(session_id, request_options=request_options).unwrap()

    def execute_browser_code(
        self,
        session_id: str,
        body: InteractExecuteRequest | InteractExecuteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InteractExecuteResponse:
        """Send a ``POST`` request.

        Args:
            session_id: The interact session ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code executed successfully

        Raises:
            ApiError: Payment required ``error`` is ``InteractExecute402Error1 | RawError``."""
        return self._with_raw_response.execute_browser_code(session_id, body, request_options=request_options).unwrap()

    def list_browser_sessions(
        self, *, status: Status10OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InteractResponse1:
        """Send a ``GET`` request.

        Args:
            status: Filter sessions by status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of interact sessions

        Raises:
            ApiError: Payment required ``error`` is ``Interact402Error1 | RawError``."""
        return self._with_raw_response.list_browser_sessions(status=status, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InteractWithRawResponse:
        return self._with_raw_response


class AsyncInteract:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInteractWithRawResponse(client, server, auth)

    async def create_browser_session(
        self, body: InteractRequest | InteractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> InteractResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interact session created successfully

        Raises:
            ApiError: Payment required ``error`` is ``Interact402Error1 | RawError``."""
        return (await self._with_raw_response.create_browser_session(body, request_options=request_options)).unwrap()

    async def delete_browser_session(
        self, session_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InteractResponse2:
        """Send a ``DELETE`` request.

        Args:
            session_id: The interact session ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Interact session deleted successfully

        Raises:
            ApiError: Payment required ``error`` is ``Interact402Error1 | RawError``."""
        return (
            await self._with_raw_response.delete_browser_session(session_id, request_options=request_options)
        ).unwrap()

    async def execute_browser_code(
        self,
        session_id: str,
        body: InteractExecuteRequest | InteractExecuteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InteractExecuteResponse:
        """Send a ``POST`` request.

        Args:
            session_id: The interact session ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code executed successfully

        Raises:
            ApiError: Payment required ``error`` is ``InteractExecute402Error1 | RawError``."""
        return (
            await self._with_raw_response.execute_browser_code(session_id, body, request_options=request_options)
        ).unwrap()

    async def list_browser_sessions(
        self, *, status: Status10OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InteractResponse1:
        """Send a ``GET`` request.

        Args:
            status: Filter sessions by status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of interact sessions

        Raises:
            ApiError: Payment required ``error`` is ``Interact402Error1 | RawError``."""
        return (
            await self._with_raw_response.list_browser_sessions(status=status, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInteractWithRawResponse:
        return self._with_raw_response


class InteractWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_browser_session(
        self, body: InteractRequest | InteractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InteractResponse, CreateBrowserSessionErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/interact"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InteractRequest | InteractRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractResponse],
            error_mapper=create_browser_session_error_mapper,
            request_options=request_options,
        )

    def delete_browser_session(
        self, session_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InteractResponse2, DeleteBrowserSessionErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            session_id: The interact session ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/interact/{sessionId}"),
            path_params=[param[str]("sessionId", session_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractResponse2],
            error_mapper=delete_browser_session_error_mapper,
            request_options=request_options,
        )

    def execute_browser_code(
        self,
        session_id: str,
        body: InteractExecuteRequest | InteractExecuteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InteractExecuteResponse, ExecuteBrowserCodeErrorBody]:
        """Send a ``POST`` request.

        Args:
            session_id: The interact session ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/interact/{sessionId}/execute"),
            path_params=[param[str]("sessionId", session_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InteractExecuteRequest | InteractExecuteRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractExecuteResponse],
            error_mapper=execute_browser_code_error_mapper,
            request_options=request_options,
        )

    def list_browser_sessions(
        self, *, status: Status10OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InteractResponse1, ListBrowserSessionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            status: Filter sessions by status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/interact"),
            query_params=[param[Status10OrStr | None]("status", status)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractResponse1],
            error_mapper=list_browser_sessions_error_mapper,
            request_options=request_options,
        )


class AsyncInteractWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_browser_session(
        self, body: InteractRequest | InteractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InteractResponse, CreateBrowserSessionErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/interact"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InteractRequest | InteractRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractResponse],
            error_mapper=create_browser_session_error_mapper,
            request_options=request_options,
        )

    async def delete_browser_session(
        self, session_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InteractResponse2, DeleteBrowserSessionErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            session_id: The interact session ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/interact/{sessionId}"),
            path_params=[param[str]("sessionId", session_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractResponse2],
            error_mapper=delete_browser_session_error_mapper,
            request_options=request_options,
        )

    async def execute_browser_code(
        self,
        session_id: str,
        body: InteractExecuteRequest | InteractExecuteRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InteractExecuteResponse, ExecuteBrowserCodeErrorBody]:
        """Send a ``POST`` request.

        Args:
            session_id: The interact session ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/interact/{sessionId}/execute"),
            path_params=[param[str]("sessionId", session_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InteractExecuteRequest | InteractExecuteRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractExecuteResponse],
            error_mapper=execute_browser_code_error_mapper,
            request_options=request_options,
        )

    async def list_browser_sessions(
        self, *, status: Status10OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InteractResponse1, ListBrowserSessionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            status: Filter sessions by status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/interact"),
            query_params=[param[Status10OrStr | None]("status", status)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[InteractResponse1],
            error_mapper=list_browser_sessions_error_mapper,
            request_options=request_options,
        )
