from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
)
from ..errors.ask_support_agent_error import AskSupportAgentErrorBody, ask_support_agent_error_mapper
from ..errors.search_support_docs_error import SearchSupportDocsErrorBody, search_support_docs_error_mapper
from ..models.support_ask_request import SupportAskRequest, SupportAskRequestDict
from ..models.support_ask_response import SupportAskResponse
from ..models.support_docs_search_request import SupportDocsSearchRequest, SupportDocsSearchRequestDict
from ..models.support_docs_search_response import SupportDocsSearchResponse
from ..server.server import Server


class Support:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SupportWithRawResponse(client, server, auth)

    def ask_support_agent(
        self, body: SupportAskRequest | SupportAskRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupportAskResponse:
        """Diagnose Firecrawl job, account, and API usage issues with an AI support agent.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Support agent answer

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Support agent unavailable Support agent timeout
                ``error`` is ``SupportProxyErrorResponse | RawError``."""
        return self._with_raw_response.ask_support_agent(body, request_options=request_options).unwrap()

    def search_support_docs(
        self,
        body: SupportDocsSearchRequest | SupportDocsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SupportDocsSearchResponse:
        """Answer Firecrawl documentation questions using the public docs corpus.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Docs-grounded answer

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Support agent unavailable Support agent timeout
                ``error`` is ``SupportProxyErrorResponse | RawError``."""
        return self._with_raw_response.search_support_docs(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SupportWithRawResponse:
        return self._with_raw_response


class AsyncSupport:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSupportWithRawResponse(client, server, auth)

    async def ask_support_agent(
        self, body: SupportAskRequest | SupportAskRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupportAskResponse:
        """Diagnose Firecrawl job, account, and API usage issues with an AI support agent.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Support agent answer

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Support agent unavailable Support agent timeout
                ``error`` is ``SupportProxyErrorResponse | RawError``."""
        return (await self._with_raw_response.ask_support_agent(body, request_options=request_options)).unwrap()

    async def search_support_docs(
        self,
        body: SupportDocsSearchRequest | SupportDocsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SupportDocsSearchResponse:
        """Answer Firecrawl documentation questions using the public docs corpus.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Docs-grounded answer

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Support agent unavailable Support agent timeout
                ``error`` is ``SupportProxyErrorResponse | RawError``."""
        return (await self._with_raw_response.search_support_docs(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSupportWithRawResponse:
        return self._with_raw_response


class SupportWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def ask_support_agent(
        self, body: SupportAskRequest | SupportAskRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupportAskResponse, AskSupportAgentErrorBody]:
        """Diagnose Firecrawl job, account, and API usage issues with an AI support agent.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/support/ask"),
            body=json_body[SupportAskRequest | SupportAskRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SupportAskResponse],
            error_mapper=ask_support_agent_error_mapper,
            request_options=request_options,
        )

    def search_support_docs(
        self,
        body: SupportDocsSearchRequest | SupportDocsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SupportDocsSearchResponse, SearchSupportDocsErrorBody]:
        """Answer Firecrawl documentation questions using the public docs corpus.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/support/docs-search"),
            body=json_body[SupportDocsSearchRequest | SupportDocsSearchRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SupportDocsSearchResponse],
            error_mapper=search_support_docs_error_mapper,
            request_options=request_options,
        )


class AsyncSupportWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def ask_support_agent(
        self, body: SupportAskRequest | SupportAskRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupportAskResponse, AskSupportAgentErrorBody]:
        """Diagnose Firecrawl job, account, and API usage issues with an AI support agent.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/support/ask"),
            body=json_body[SupportAskRequest | SupportAskRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SupportAskResponse],
            error_mapper=ask_support_agent_error_mapper,
            request_options=request_options,
        )

    async def search_support_docs(
        self,
        body: SupportDocsSearchRequest | SupportDocsSearchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SupportDocsSearchResponse, SearchSupportDocsErrorBody]:
        """Answer Firecrawl documentation questions using the public docs corpus.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/support/docs-search"),
            body=json_body[SupportDocsSearchRequest | SupportDocsSearchRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SupportDocsSearchResponse],
            error_mapper=search_support_docs_error_mapper,
            request_options=request_options,
        )
