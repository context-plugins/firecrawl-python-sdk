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
    param,
)
from ..errors.developer_search_error import DeveloperSearchErrorBody, developer_search_error_mapper
from ..errors.developer_search_post_error import DeveloperSearchPostErrorBody, developer_search_post_error_mapper
from ..models.developer_search_response import DeveloperSearchResponse
from ..models.enums.skills import SkillsOrStr
from ..models.enums.types1 import Types1OrStr
from ..models.search_developer_request import SearchDeveloperRequest, SearchDeveloperRequestDict
from ..server.server import Server


class Developer:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeveloperWithRawResponse(client, server, auth)

    def developer_search(
        self,
        query: str,
        *,
        k: int | None = 10,
        types: list[Types1OrStr] | None = None,
        repos: list[str] | None = None,
        sources: list[str] | None = None,
        skills: SkillsOrStr | None = None,
        passages: int | None = 1,
        language: str | None = None,
        topic: str | None = None,
        license: str | None = None,
        min_stars: int | None = None,
        max_stars: int | None = None,
        archived: bool | None = None,
        fork: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeveloperSearchResponse:
        """Send a ``GET`` request.

        Args:
            query: Natural-language question or search phrase.
            k: Number of ranked results to return.
            types: Result kinds to search. Defaults to all four. Accepts a repeated parameter
                (``types=issue&types=pull_request``) or one comma-separated value (``types=issue,pull_request``).
            repos: Repository slugs to scope the repository half of the index to, such as ``firecrawl/firecrawl``.
                Applies to the ``issue``, ``pull_request``, and ``readme`` types only. Sent together with ``sources``,
                the two halves are combined rather than intersected, so matching results come back from either. Returns
                400 when no repository type is in ``types``, reporting that ``repos`` cannot match any requested type
                and that you should add repository types or drop ``repos``.
            sources: Documentation source ids to scope the documentation half to, at most 20. Applies to the ``doc``
                type only. Not a fixed enum: ids reflect the documentation sites in the index and the set grows over
                time, so confirm an id resolves by sending it and reading the ``sources`` array on the response. Returns
                400 with ``sources cannot match any requested type; add doc or drop sources`` when ``doc`` is not in
                ``types``.
            skills: Set to ``only`` to limit the search to indexed agent-skill files.
            passages: Matched passages to return per result.
            language: Repository primary language, such as ``Rust``. Applies to repository results only; sending it with
                no ``sources`` scope returns no ``doc`` results. See `how the repository filters scope a search
                </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__.
            topic: Repository topic, such as ``async``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            license: Repository license, such as ``MIT``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            min_stars: Lower bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            max_stars: Upper bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            archived: Include or exclude archived repositories. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            fork: Include or exclude forks. Applies to repository results only; sending it with no ``sources`` scope
                returns no ``doc`` results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked developer results with matched passages.

        Raises:
            ApiError: Invalid request, including a filter that cannot match any requested type Missing or invalid bearer
                token Rate limit exceeded Internal server error ``error`` is ``RawError``."""
        return self._with_raw_response.developer_search(
            query,
            k=k,
            types=types,
            repos=repos,
            sources=sources,
            skills=skills,
            passages=passages,
            language=language,
            topic=topic,
            license=license,
            min_stars=min_stars,
            max_stars=max_stars,
            archived=archived,
            fork=fork,
            request_options=request_options,
        ).unwrap()

    def developer_search_post(
        self,
        body: SearchDeveloperRequest | SearchDeveloperRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeveloperSearchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked developer results with matched passages.

        Raises:
            ApiError: Invalid request, including a filter that cannot match any requested type Missing or invalid bearer
                token Rate limit exceeded Internal server error ``error`` is ``RawError``."""
        return self._with_raw_response.developer_search_post(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeveloperWithRawResponse:
        return self._with_raw_response


class AsyncDeveloper:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeveloperWithRawResponse(client, server, auth)

    async def developer_search(
        self,
        query: str,
        *,
        k: int | None = 10,
        types: list[Types1OrStr] | None = None,
        repos: list[str] | None = None,
        sources: list[str] | None = None,
        skills: SkillsOrStr | None = None,
        passages: int | None = 1,
        language: str | None = None,
        topic: str | None = None,
        license: str | None = None,
        min_stars: int | None = None,
        max_stars: int | None = None,
        archived: bool | None = None,
        fork: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeveloperSearchResponse:
        """Send a ``GET`` request.

        Args:
            query: Natural-language question or search phrase.
            k: Number of ranked results to return.
            types: Result kinds to search. Defaults to all four. Accepts a repeated parameter
                (``types=issue&types=pull_request``) or one comma-separated value (``types=issue,pull_request``).
            repos: Repository slugs to scope the repository half of the index to, such as ``firecrawl/firecrawl``.
                Applies to the ``issue``, ``pull_request``, and ``readme`` types only. Sent together with ``sources``,
                the two halves are combined rather than intersected, so matching results come back from either. Returns
                400 when no repository type is in ``types``, reporting that ``repos`` cannot match any requested type
                and that you should add repository types or drop ``repos``.
            sources: Documentation source ids to scope the documentation half to, at most 20. Applies to the ``doc``
                type only. Not a fixed enum: ids reflect the documentation sites in the index and the set grows over
                time, so confirm an id resolves by sending it and reading the ``sources`` array on the response. Returns
                400 with ``sources cannot match any requested type; add doc or drop sources`` when ``doc`` is not in
                ``types``.
            skills: Set to ``only`` to limit the search to indexed agent-skill files.
            passages: Matched passages to return per result.
            language: Repository primary language, such as ``Rust``. Applies to repository results only; sending it with
                no ``sources`` scope returns no ``doc`` results. See `how the repository filters scope a search
                </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__.
            topic: Repository topic, such as ``async``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            license: Repository license, such as ``MIT``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            min_stars: Lower bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            max_stars: Upper bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            archived: Include or exclude archived repositories. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            fork: Include or exclude forks. Applies to repository results only; sending it with no ``sources`` scope
                returns no ``doc`` results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked developer results with matched passages.

        Raises:
            ApiError: Invalid request, including a filter that cannot match any requested type Missing or invalid bearer
                token Rate limit exceeded Internal server error ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.developer_search(
                query,
                k=k,
                types=types,
                repos=repos,
                sources=sources,
                skills=skills,
                passages=passages,
                language=language,
                topic=topic,
                license=license,
                min_stars=min_stars,
                max_stars=max_stars,
                archived=archived,
                fork=fork,
                request_options=request_options,
            )
        ).unwrap()

    async def developer_search_post(
        self,
        body: SearchDeveloperRequest | SearchDeveloperRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeveloperSearchResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Ranked developer results with matched passages.

        Raises:
            ApiError: Invalid request, including a filter that cannot match any requested type Missing or invalid bearer
                token Rate limit exceeded Internal server error ``error`` is ``RawError``."""
        return (await self._with_raw_response.developer_search_post(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeveloperWithRawResponse:
        return self._with_raw_response


class DeveloperWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def developer_search(
        self,
        query: str,
        *,
        k: int | None = 10,
        types: list[Types1OrStr] | None = None,
        repos: list[str] | None = None,
        sources: list[str] | None = None,
        skills: SkillsOrStr | None = None,
        passages: int | None = 1,
        language: str | None = None,
        topic: str | None = None,
        license: str | None = None,
        min_stars: int | None = None,
        max_stars: int | None = None,
        archived: bool | None = None,
        fork: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeveloperSearchResponse, DeveloperSearchErrorBody]:
        """Send a ``GET`` request.

        Args:
            query: Natural-language question or search phrase.
            k: Number of ranked results to return.
            types: Result kinds to search. Defaults to all four. Accepts a repeated parameter
                (``types=issue&types=pull_request``) or one comma-separated value (``types=issue,pull_request``).
            repos: Repository slugs to scope the repository half of the index to, such as ``firecrawl/firecrawl``.
                Applies to the ``issue``, ``pull_request``, and ``readme`` types only. Sent together with ``sources``,
                the two halves are combined rather than intersected, so matching results come back from either. Returns
                400 when no repository type is in ``types``, reporting that ``repos`` cannot match any requested type
                and that you should add repository types or drop ``repos``.
            sources: Documentation source ids to scope the documentation half to, at most 20. Applies to the ``doc``
                type only. Not a fixed enum: ids reflect the documentation sites in the index and the set grows over
                time, so confirm an id resolves by sending it and reading the ``sources`` array on the response. Returns
                400 with ``sources cannot match any requested type; add doc or drop sources`` when ``doc`` is not in
                ``types``.
            skills: Set to ``only`` to limit the search to indexed agent-skill files.
            passages: Matched passages to return per result.
            language: Repository primary language, such as ``Rust``. Applies to repository results only; sending it with
                no ``sources`` scope returns no ``doc`` results. See `how the repository filters scope a search
                </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__.
            topic: Repository topic, such as ``async``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            license: Repository license, such as ``MIT``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            min_stars: Lower bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            max_stars: Upper bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            archived: Include or exclude archived repositories. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            fork: Include or exclude forks. Applies to repository results only; sending it with no ``sources`` scope
                returns no ``doc`` results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/developer"),
            query_params=[
                param[str]("query", query),
                param[int | None]("k", k),
                param[list[Types1OrStr] | None]("types", types),
                param[list[str] | None]("repos", repos),
                param[list[str] | None]("sources", sources),
                param[SkillsOrStr | None]("skills", skills),
                param[int | None]("passages", passages),
                param[str | None]("language", language),
                param[str | None]("topic", topic),
                param[str | None]("license", license),
                param[int | None]("min_stars", min_stars),
                param[int | None]("max_stars", max_stars),
                param[bool | None]("archived", archived),
                param[bool | None]("fork", fork),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[DeveloperSearchResponse],
            error_mapper=developer_search_error_mapper,
            request_options=request_options,
        )

    def developer_search_post(
        self,
        body: SearchDeveloperRequest | SearchDeveloperRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeveloperSearchResponse, DeveloperSearchPostErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/search/developer"),
            body=json_body[SearchDeveloperRequest | SearchDeveloperRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[DeveloperSearchResponse],
            error_mapper=developer_search_post_error_mapper,
            request_options=request_options,
        )


class AsyncDeveloperWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def developer_search(
        self,
        query: str,
        *,
        k: int | None = 10,
        types: list[Types1OrStr] | None = None,
        repos: list[str] | None = None,
        sources: list[str] | None = None,
        skills: SkillsOrStr | None = None,
        passages: int | None = 1,
        language: str | None = None,
        topic: str | None = None,
        license: str | None = None,
        min_stars: int | None = None,
        max_stars: int | None = None,
        archived: bool | None = None,
        fork: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeveloperSearchResponse, DeveloperSearchErrorBody]:
        """Send a ``GET`` request.

        Args:
            query: Natural-language question or search phrase.
            k: Number of ranked results to return.
            types: Result kinds to search. Defaults to all four. Accepts a repeated parameter
                (``types=issue&types=pull_request``) or one comma-separated value (``types=issue,pull_request``).
            repos: Repository slugs to scope the repository half of the index to, such as ``firecrawl/firecrawl``.
                Applies to the ``issue``, ``pull_request``, and ``readme`` types only. Sent together with ``sources``,
                the two halves are combined rather than intersected, so matching results come back from either. Returns
                400 when no repository type is in ``types``, reporting that ``repos`` cannot match any requested type
                and that you should add repository types or drop ``repos``.
            sources: Documentation source ids to scope the documentation half to, at most 20. Applies to the ``doc``
                type only. Not a fixed enum: ids reflect the documentation sites in the index and the set grows over
                time, so confirm an id resolves by sending it and reading the ``sources`` array on the response. Returns
                400 with ``sources cannot match any requested type; add doc or drop sources`` when ``doc`` is not in
                ``types``.
            skills: Set to ``only`` to limit the search to indexed agent-skill files.
            passages: Matched passages to return per result.
            language: Repository primary language, such as ``Rust``. Applies to repository results only; sending it with
                no ``sources`` scope returns no ``doc`` results. See `how the repository filters scope a search
                </api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search>`__.
            topic: Repository topic, such as ``async``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            license: Repository license, such as ``MIT``. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            min_stars: Lower bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            max_stars: Upper bound on repository stars. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            archived: Include or exclude archived repositories. Applies to repository results only; sending it with no
                ``sources`` scope returns no ``doc`` results.
            fork: Include or exclude forks. Applies to repository results only; sending it with no ``sources`` scope
                returns no ``doc`` results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/search/developer"),
            query_params=[
                param[str]("query", query),
                param[int | None]("k", k),
                param[list[Types1OrStr] | None]("types", types),
                param[list[str] | None]("repos", repos),
                param[list[str] | None]("sources", sources),
                param[SkillsOrStr | None]("skills", skills),
                param[int | None]("passages", passages),
                param[str | None]("language", language),
                param[str | None]("topic", topic),
                param[str | None]("license", license),
                param[int | None]("min_stars", min_stars),
                param[int | None]("max_stars", max_stars),
                param[bool | None]("archived", archived),
                param[bool | None]("fork", fork),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[DeveloperSearchResponse],
            error_mapper=developer_search_error_mapper,
            request_options=request_options,
        )

    async def developer_search_post(
        self,
        body: SearchDeveloperRequest | SearchDeveloperRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeveloperSearchResponse, DeveloperSearchPostErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/search/developer"),
            body=json_body[SearchDeveloperRequest | SearchDeveloperRequestDict](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[DeveloperSearchResponse],
            error_mapper=developer_search_post_error_mapper,
            request_options=request_options,
        )
