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
from ..errors.create_monitor_error import CreateMonitorErrorBody, create_monitor_error_mapper
from ..errors.delete_monitor_error import DeleteMonitorErrorBody, delete_monitor_error_mapper
from ..errors.get_monitor_check_error import GetMonitorCheckErrorBody, get_monitor_check_error_mapper
from ..errors.get_monitor_error import GetMonitorErrorBody, get_monitor_error_mapper
from ..errors.run_monitor_error import RunMonitorErrorBody, run_monitor_error_mapper
from ..errors.update_monitor_error import UpdateMonitorErrorBody, update_monitor_error_mapper
from ..models.enums.status2 import Status2OrStr
from ..models.enums.status3 import Status3OrStr
from ..models.monitor_check_detail_response import MonitorCheckDetailResponse
from ..models.monitor_check_list_response import MonitorCheckListResponse
from ..models.monitor_create_request import MonitorCreateRequest, MonitorCreateRequestDict
from ..models.monitor_list_response import MonitorListResponse
from ..models.monitor_response import MonitorResponse
from ..models.monitor_run_response import MonitorRunResponse
from ..models.monitor_update_request import MonitorUpdateRequest, MonitorUpdateRequestDict
from ..models.success_response import SuccessResponse
from ..server.server import Server


class Monitoring:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MonitoringWithRawResponse(client, server, auth)

    def create_monitor(
        self,
        body: MonitorCreateRequest | MonitorCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor created

        Raises:
            ApiError: Invalid monitor request ``error`` is ``RawError``."""
        return self._with_raw_response.create_monitor(body, request_options=request_options).unwrap()

    def delete_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor deleted

        Raises:
            ApiError: Monitor not found ``error`` is ``RawError``."""
        return self._with_raw_response.delete_monitor(monitor_id, request_options=request_options).unwrap()

    def get_monitor(self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> MonitorResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor details

        Raises:
            ApiError: Monitor not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_monitor(monitor_id, request_options=request_options).unwrap()

    def get_monitor_check(
        self,
        monitor_id: UUID,
        check_id: UUID,
        *,
        limit: int | None = 25,
        skip: int | None = 0,
        status: Status3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorCheckDetailResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            check_id: The monitor check ID
            limit: Value sent with the request.
            skip: Number of page results to skip. Use the ``next`` URL from the previous response for pagination.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor check details

        Raises:
            ApiError: Monitor check not found ``error`` is ``RawError``."""
        return self._with_raw_response.get_monitor_check(
            monitor_id, check_id, limit=limit, skip=skip, status=status, request_options=request_options
        ).unwrap()

    def list_monitor_checks(
        self,
        monitor_id: UUID,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorCheckListResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            limit: Value sent with the request.
            offset: Value sent with the request.
            status: Filter checks by status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor checks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_monitor_checks(
            monitor_id, limit=limit, offset=offset, status=status, request_options=request_options
        ).unwrap()

    def list_monitors(
        self, *, limit: int | None = 25, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> MonitorListResponse:
        """Send a ``GET`` request.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of monitors

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_monitors(
            limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def run_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> MonitorRunResponse:
        """Send a ``POST`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor check queued

        Raises:
            ApiError: A monitor check is already running ``error`` is ``RawError``."""
        return self._with_raw_response.run_monitor(monitor_id, request_options=request_options).unwrap()

    def update_monitor(
        self,
        monitor_id: UUID,
        body: MonitorUpdateRequest | MonitorUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorResponse:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: The monitor ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor updated

        Raises:
            ApiError: Monitor not found ``error`` is ``RawError``."""
        return self._with_raw_response.update_monitor(monitor_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MonitoringWithRawResponse:
        return self._with_raw_response


class AsyncMonitoring:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMonitoringWithRawResponse(client, server, auth)

    async def create_monitor(
        self,
        body: MonitorCreateRequest | MonitorCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor created

        Raises:
            ApiError: Invalid monitor request ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_monitor(body, request_options=request_options)).unwrap()

    async def delete_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor deleted

        Raises:
            ApiError: Monitor not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_monitor(monitor_id, request_options=request_options)).unwrap()

    async def get_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> MonitorResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor details

        Raises:
            ApiError: Monitor not found ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_monitor(monitor_id, request_options=request_options)).unwrap()

    async def get_monitor_check(
        self,
        monitor_id: UUID,
        check_id: UUID,
        *,
        limit: int | None = 25,
        skip: int | None = 0,
        status: Status3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorCheckDetailResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            check_id: The monitor check ID
            limit: Value sent with the request.
            skip: Number of page results to skip. Use the ``next`` URL from the previous response for pagination.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor check details

        Raises:
            ApiError: Monitor check not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_monitor_check(
                monitor_id, check_id, limit=limit, skip=skip, status=status, request_options=request_options
            )
        ).unwrap()

    async def list_monitor_checks(
        self,
        monitor_id: UUID,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorCheckListResponse:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            limit: Value sent with the request.
            offset: Value sent with the request.
            status: Filter checks by status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor checks

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_monitor_checks(
                monitor_id, limit=limit, offset=offset, status=status, request_options=request_options
            )
        ).unwrap()

    async def list_monitors(
        self, *, limit: int | None = 25, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> MonitorListResponse:
        """Send a ``GET`` request.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of monitors

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_monitors(limit=limit, offset=offset, request_options=request_options)
        ).unwrap()

    async def run_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> MonitorRunResponse:
        """Send a ``POST`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor check queued

        Raises:
            ApiError: A monitor check is already running ``error`` is ``RawError``."""
        return (await self._with_raw_response.run_monitor(monitor_id, request_options=request_options)).unwrap()

    async def update_monitor(
        self,
        monitor_id: UUID,
        body: MonitorUpdateRequest | MonitorUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MonitorResponse:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: The monitor ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Monitor updated

        Raises:
            ApiError: Monitor not found ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_monitor(monitor_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMonitoringWithRawResponse:
        return self._with_raw_response


class MonitoringWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_monitor(
        self,
        body: MonitorCreateRequest | MonitorCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorResponse, CreateMonitorErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/monitor"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MonitorCreateRequest | MonitorCreateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorResponse],
            error_mapper=create_monitor_error_mapper,
            request_options=request_options,
        )

    def delete_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, DeleteMonitorErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/monitor/{monitorId}"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SuccessResponse],
            error_mapper=delete_monitor_error_mapper,
            request_options=request_options,
        )

    def get_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MonitorResponse, GetMonitorErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor/{monitorId}"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorResponse],
            error_mapper=get_monitor_error_mapper,
            request_options=request_options,
        )

    def get_monitor_check(
        self,
        monitor_id: UUID,
        check_id: UUID,
        *,
        limit: int | None = 25,
        skip: int | None = 0,
        status: Status3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorCheckDetailResponse, GetMonitorCheckErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            check_id: The monitor check ID
            limit: Value sent with the request.
            skip: Number of page results to skip. Use the ``next`` URL from the previous response for pagination.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor/{monitorId}/checks/{checkId}"),
            path_params=[param[UUID]("monitorId", monitor_id), param[UUID]("checkId", check_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("skip", skip),
                param[Status3OrStr | None]("status", status),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorCheckDetailResponse],
            error_mapper=get_monitor_check_error_mapper,
            request_options=request_options,
        )

    def list_monitor_checks(
        self,
        monitor_id: UUID,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorCheckListResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            limit: Value sent with the request.
            offset: Value sent with the request.
            status: Filter checks by status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor/{monitorId}/checks"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[Status2OrStr | None]("status", status),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorCheckListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_monitors(
        self, *, limit: int | None = 25, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MonitorListResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def run_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MonitorRunResponse, RunMonitorErrorBody]:
        """Send a ``POST`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/monitor/{monitorId}/run"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorRunResponse],
            error_mapper=run_monitor_error_mapper,
            request_options=request_options,
        )

    def update_monitor(
        self,
        monitor_id: UUID,
        body: MonitorUpdateRequest | MonitorUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorResponse, UpdateMonitorErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: The monitor ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/monitor/{monitorId}"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MonitorUpdateRequest | MonitorUpdateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorResponse],
            error_mapper=update_monitor_error_mapper,
            request_options=request_options,
        )


class AsyncMonitoringWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_monitor(
        self,
        body: MonitorCreateRequest | MonitorCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorResponse, CreateMonitorErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/monitor"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MonitorCreateRequest | MonitorCreateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorResponse],
            error_mapper=create_monitor_error_mapper,
            request_options=request_options,
        )

    async def delete_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, DeleteMonitorErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/monitor/{monitorId}"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SuccessResponse],
            error_mapper=delete_monitor_error_mapper,
            request_options=request_options,
        )

    async def get_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MonitorResponse, GetMonitorErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor/{monitorId}"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorResponse],
            error_mapper=get_monitor_error_mapper,
            request_options=request_options,
        )

    async def get_monitor_check(
        self,
        monitor_id: UUID,
        check_id: UUID,
        *,
        limit: int | None = 25,
        skip: int | None = 0,
        status: Status3OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorCheckDetailResponse, GetMonitorCheckErrorBody]:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            check_id: The monitor check ID
            limit: Value sent with the request.
            skip: Number of page results to skip. Use the ``next`` URL from the previous response for pagination.
            status: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor/{monitorId}/checks/{checkId}"),
            path_params=[param[UUID]("monitorId", monitor_id), param[UUID]("checkId", check_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("skip", skip),
                param[Status3OrStr | None]("status", status),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorCheckDetailResponse],
            error_mapper=get_monitor_check_error_mapper,
            request_options=request_options,
        )

    async def list_monitor_checks(
        self,
        monitor_id: UUID,
        *,
        limit: int | None = 25,
        offset: int | None = 0,
        status: Status2OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorCheckListResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            monitor_id: The monitor ID
            limit: Value sent with the request.
            offset: Value sent with the request.
            status: Filter checks by status.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor/{monitorId}/checks"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[Status2OrStr | None]("status", status),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorCheckListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_monitors(
        self, *, limit: int | None = 25, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MonitorListResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            limit: Value sent with the request.
            offset: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/monitor"),
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def run_monitor(
        self, monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MonitorRunResponse, RunMonitorErrorBody]:
        """Send a ``POST`` request.

        Args:
            monitor_id: The monitor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/monitor/{monitorId}/run"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorRunResponse],
            error_mapper=run_monitor_error_mapper,
            request_options=request_options,
        )

    async def update_monitor(
        self,
        monitor_id: UUID,
        body: MonitorUpdateRequest | MonitorUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MonitorResponse, UpdateMonitorErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            monitor_id: The monitor ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/monitor/{monitorId}"),
            path_params=[param[UUID]("monitorId", monitor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MonitorUpdateRequest | MonitorUpdateRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MonitorResponse],
            error_mapper=update_monitor_error_mapper,
            request_options=request_options,
        )
