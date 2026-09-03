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
from ..errors.extract_data_error import ExtractDataErrorBody, extract_data_error_mapper
from ..models.extract_request import ExtractRequest, ExtractRequestDict
from ..models.extract_response import ExtractResponse
from ..models.extract_status_response import ExtractStatusResponse
from ..server.server import Server


class Extraction:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ExtractionWithRawResponse(client, server, auth)

    def extract_data(
        self, body: ExtractRequest | ExtractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExtractResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful extraction

        Raises:
            ApiError: Invalid request Server error ``error`` is ``Extract400Error1 | Extract500Error1 | RawError``."""
        return self._with_raw_response.extract_data(body, request_options=request_options).unwrap()

    def get_extract_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExtractStatusResponse:
        """Send a ``GET`` request.

        Args:
            id: The ID of the extract job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_extract_status(id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ExtractionWithRawResponse:
        return self._with_raw_response


class AsyncExtraction:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncExtractionWithRawResponse(client, server, auth)

    async def extract_data(
        self, body: ExtractRequest | ExtractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExtractResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful extraction

        Raises:
            ApiError: Invalid request Server error ``error`` is ``Extract400Error1 | Extract500Error1 | RawError``."""
        return (await self._with_raw_response.extract_data(body, request_options=request_options)).unwrap()

    async def get_extract_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExtractStatusResponse:
        """Send a ``GET`` request.

        Args:
            id: The ID of the extract job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_extract_status(id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncExtractionWithRawResponse:
        return self._with_raw_response


class ExtractionWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def extract_data(
        self, body: ExtractRequest | ExtractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExtractResponse, ExtractDataErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/extract"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ExtractRequest | ExtractRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ExtractResponse],
            error_mapper=extract_data_error_mapper,
            request_options=request_options,
        )

    def get_extract_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExtractStatusResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the extract job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/extract/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ExtractStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncExtractionWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def extract_data(
        self, body: ExtractRequest | ExtractRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExtractResponse, ExtractDataErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/extract"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ExtractRequest | ExtractRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ExtractResponse],
            error_mapper=extract_data_error_mapper,
            request_options=request_options,
        )

    async def get_extract_status(
        self, id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExtractStatusResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id: The ID of the extract job
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/extract/{id}"),
            path_params=[param[UUID]("id", id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ExtractStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
