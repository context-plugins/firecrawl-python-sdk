from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.research_get_paper_error import ResearchGetPaperErrorBody, research_get_paper_error_mapper
from ..errors.research_related_papers_error import ResearchRelatedPapersErrorBody, research_related_papers_error_mapper
from ..errors.research_search_papers_error import ResearchSearchPapersErrorBody, research_search_papers_error_mapper
from ..models.enums.mode5 import Mode5OrStr
from ..models.research_search_papers_response import ResearchSearchPapersResponse
from ..models.research_similar_papers_response import ResearchSimilarPapersResponse
from ..models.unions.search_research_papers_response import SearchResearchPapersResponse
from ..server.server import Server


class ResearchApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ResearchApiWithRawResponse(client, server, auth)

    def research_get_paper(
        self,
        id: str,
        *,
        query: str | None = None,
        k: int | None = 4,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchResearchPapersResponse:
        """Send a ``GET`` request.

        Args:
            id: Paper reference: a canonical paperId or source-specific primaryId.
            query: When present, returns the top matching full-text passages for this question. Omit it to inspect
                metadata only.
            k: Passage count for read mode. Only valid when query is present.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Paper metadata or read-mode passages.

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Paper not found Rate limit exceeded Internal
                server error ``error`` is ``RawError``."""
        return self._with_raw_response.research_get_paper(
            id, query=query, k=k, request_options=request_options
        ).unwrap()

    def research_related_papers(
        self,
        id: str,
        intent: str,
        *,
        mode: Mode5OrStr | None = None,
        k: int | None = 40,
        rerank: bool | None = None,
        anchor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResearchSimilarPapersResponse:
        """Send a ``GET`` request.

        Args:
            id: Primary seed paper reference.
            intent: Natural-language ranking/filtering intent used for semantic ranking.
            mode: Structural expansion mode.
            k: Maximum number of related papers to return.
            rerank: Apply an additional rerank over fused candidates.
            anchor: Additional seed paper reference. Repeat this parameter for multiple anchors.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked related papers.

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Rate limit exceeded Internal server error
                ``error`` is ``RawError``."""
        return self._with_raw_response.research_related_papers(
            id, intent, mode=mode, k=k, rerank=rerank, anchor=anchor, request_options=request_options
        ).unwrap()

    def research_search_papers(
        self,
        query: str,
        *,
        k: int | None = 40,
        authors: str | None = None,
        categories: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResearchSearchPapersResponse:
        """Send a ``GET`` request.

        Args:
            query: Natural-language paper search query.
            k: Maximum number of ranked papers to return.
            authors: Author substring filter. Repeat or pass a comma-separated value; all filters must match.
            categories: Paper category filter. Repeat or pass a comma-separated value; all filters must match.
            from_: Inclusive lower bound on created/updated date.
            to: Inclusive upper bound on created/updated date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked paper results.

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Rate limit exceeded Internal server error
                ``error`` is ``RawError``."""
        return self._with_raw_response.research_search_papers(
            query, k=k, authors=authors, categories=categories, from_=from_, to=to, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ResearchApiWithRawResponse:
        return self._with_raw_response


class AsyncResearchApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncResearchApiWithRawResponse(client, server, auth)

    async def research_get_paper(
        self,
        id: str,
        *,
        query: str | None = None,
        k: int | None = 4,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchResearchPapersResponse:
        """Send a ``GET`` request.

        Args:
            id: Paper reference: a canonical paperId or source-specific primaryId.
            query: When present, returns the top matching full-text passages for this question. Omit it to inspect
                metadata only.
            k: Passage count for read mode. Only valid when query is present.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Paper metadata or read-mode passages.

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Paper not found Rate limit exceeded Internal
                server error ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.research_get_paper(id, query=query, k=k, request_options=request_options)
        ).unwrap()

    async def research_related_papers(
        self,
        id: str,
        intent: str,
        *,
        mode: Mode5OrStr | None = None,
        k: int | None = 40,
        rerank: bool | None = None,
        anchor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResearchSimilarPapersResponse:
        """Send a ``GET`` request.

        Args:
            id: Primary seed paper reference.
            intent: Natural-language ranking/filtering intent used for semantic ranking.
            mode: Structural expansion mode.
            k: Maximum number of related papers to return.
            rerank: Apply an additional rerank over fused candidates.
            anchor: Additional seed paper reference. Repeat this parameter for multiple anchors.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked related papers.

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Rate limit exceeded Internal server error
                ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.research_related_papers(
                id, intent, mode=mode, k=k, rerank=rerank, anchor=anchor, request_options=request_options
            )
        ).unwrap()

    async def research_search_papers(
        self,
        query: str,
        *,
        k: int | None = 40,
        authors: str | None = None,
        categories: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResearchSearchPapersResponse:
        """Send a ``GET`` request.

        Args:
            query: Natural-language paper search query.
            k: Maximum number of ranked papers to return.
            authors: Author substring filter. Repeat or pass a comma-separated value; all filters must match.
            categories: Paper category filter. Repeat or pass a comma-separated value; all filters must match.
            from_: Inclusive lower bound on created/updated date.
            to: Inclusive upper bound on created/updated date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked paper results.

        Raises:
            ApiError: Invalid request Missing or invalid bearer token Rate limit exceeded Internal server error
                ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.research_search_papers(
                query, k=k, authors=authors, categories=categories, from_=from_, to=to, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncResearchApiWithRawResponse:
        return self._with_raw_response


class ResearchApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def research_get_paper(
        self,
        id: str,
        *,
        query: str | None = None,
        k: int | None = 4,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchResearchPapersResponse, ResearchGetPaperErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Paper reference: a canonical paperId or source-specific primaryId.
            query: When present, returns the top matching full-text passages for this question. Omit it to inspect
                metadata only.
            k: Passage count for read mode. Only valid when query is present.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/research/papers/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("query", query), param[int | None]("k", k)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SearchResearchPapersResponse],
            error_mapper=research_get_paper_error_mapper,
            request_options=request_options,
        )

    def research_related_papers(
        self,
        id: str,
        intent: str,
        *,
        mode: Mode5OrStr | None = None,
        k: int | None = 40,
        rerank: bool | None = None,
        anchor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResearchSimilarPapersResponse, ResearchRelatedPapersErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Primary seed paper reference.
            intent: Natural-language ranking/filtering intent used for semantic ranking.
            mode: Structural expansion mode.
            k: Maximum number of related papers to return.
            rerank: Apply an additional rerank over fused candidates.
            anchor: Additional seed paper reference. Repeat this parameter for multiple anchors.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/research/papers/{id}/similar"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("intent", intent),
                param[Mode5OrStr | None]("mode", mode),
                param[int | None]("k", k),
                param[bool | None]("rerank", rerank),
                param[str | None]("anchor", anchor),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ResearchSimilarPapersResponse],
            error_mapper=research_related_papers_error_mapper,
            request_options=request_options,
        )

    def research_search_papers(
        self,
        query: str,
        *,
        k: int | None = 40,
        authors: str | None = None,
        categories: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResearchSearchPapersResponse, ResearchSearchPapersErrorBody]:
        """Send a ``GET`` request.

        Args:
            query: Natural-language paper search query.
            k: Maximum number of ranked papers to return.
            authors: Author substring filter. Repeat or pass a comma-separated value; all filters must match.
            categories: Paper category filter. Repeat or pass a comma-separated value; all filters must match.
            from_: Inclusive lower bound on created/updated date.
            to: Inclusive upper bound on created/updated date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/research/papers"),
            query_params=[
                param[str]("query", query),
                param[int | None]("k", k),
                param[str | None]("authors", authors),
                param[str | None]("categories", categories),
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ResearchSearchPapersResponse],
            error_mapper=research_search_papers_error_mapper,
            request_options=request_options,
        )


class AsyncResearchApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def research_get_paper(
        self,
        id: str,
        *,
        query: str | None = None,
        k: int | None = 4,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchResearchPapersResponse, ResearchGetPaperErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Paper reference: a canonical paperId or source-specific primaryId.
            query: When present, returns the top matching full-text passages for this question. Omit it to inspect
                metadata only.
            k: Passage count for read mode. Only valid when query is present.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/research/papers/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str | None]("query", query), param[int | None]("k", k)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SearchResearchPapersResponse],
            error_mapper=research_get_paper_error_mapper,
            request_options=request_options,
        )

    async def research_related_papers(
        self,
        id: str,
        intent: str,
        *,
        mode: Mode5OrStr | None = None,
        k: int | None = 40,
        rerank: bool | None = None,
        anchor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResearchSimilarPapersResponse, ResearchRelatedPapersErrorBody]:
        """Send a ``GET`` request.

        Args:
            id: Primary seed paper reference.
            intent: Natural-language ranking/filtering intent used for semantic ranking.
            mode: Structural expansion mode.
            k: Maximum number of related papers to return.
            rerank: Apply an additional rerank over fused candidates.
            anchor: Additional seed paper reference. Repeat this parameter for multiple anchors.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/research/papers/{id}/similar"),
            path_params=[param[str]("id", id)],
            query_params=[
                param[str]("intent", intent),
                param[Mode5OrStr | None]("mode", mode),
                param[int | None]("k", k),
                param[bool | None]("rerank", rerank),
                param[str | None]("anchor", anchor),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ResearchSimilarPapersResponse],
            error_mapper=research_related_papers_error_mapper,
            request_options=request_options,
        )

    async def research_search_papers(
        self,
        query: str,
        *,
        k: int | None = 40,
        authors: str | None = None,
        categories: str | None = None,
        from_: Date | None = None,
        to: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResearchSearchPapersResponse, ResearchSearchPapersErrorBody]:
        """Send a ``GET`` request.

        Args:
            query: Natural-language paper search query.
            k: Maximum number of ranked papers to return.
            authors: Author substring filter. Repeat or pass a comma-separated value; all filters must match.
            categories: Paper category filter. Repeat or pass a comma-separated value; all filters must match.
            from_: Inclusive lower bound on created/updated date.
            to: Inclusive upper bound on created/updated date.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/research/papers"),
            query_params=[
                param[str]("query", query),
                param[int | None]("k", k),
                param[str | None]("authors", authors),
                param[str | None]("categories", categories),
                param[Date | None]("from", from_),
                param[Date | None]("to", to),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ResearchSearchPapersResponse],
            error_mapper=research_search_papers_error_mapper,
            request_options=request_options,
        )
