from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account import AsyncAccount
from .apis.agent import AsyncAgent
from .apis.billing import AsyncBilling
from .apis.crawling import AsyncCrawling
from .apis.developer import AsyncDeveloper
from .apis.extraction import AsyncExtraction
from .apis.feedback import AsyncFeedback
from .apis.interact import AsyncInteract
from .apis.mapping_api import AsyncMappingApi
from .apis.miscellaneous import AsyncMiscellaneous
from .apis.monitoring import AsyncMonitoring
from .apis.research_api import AsyncResearchApi
from .apis.scraping import AsyncScraping
from .apis.search import AsyncSearch
from .apis.support import AsyncSupport
from .apis.threat_protection import AsyncThreatProtection
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseFirecrawlApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    BearerAuthScheme,
    no_auth,
    param,
)


class AsyncFirecrawlApiClient(BaseFirecrawlApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        bearer_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "FirecrawlApiClient/v2 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "v2"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth)

    @cached_property
    def account(self) -> AsyncAccount:
        return AsyncAccount(self._raw_client, self._server, self._auth)

    @cached_property
    def agent(self) -> AsyncAgent:
        return AsyncAgent(self._raw_client, self._server, self._auth)

    @cached_property
    def billing(self) -> AsyncBilling:
        return AsyncBilling(self._raw_client, self._server, self._auth)

    @cached_property
    def crawling(self) -> AsyncCrawling:
        return AsyncCrawling(self._raw_client, self._server, self._auth)

    @cached_property
    def developer(self) -> AsyncDeveloper:
        return AsyncDeveloper(self._raw_client, self._server, self._auth)

    @cached_property
    def extraction(self) -> AsyncExtraction:
        return AsyncExtraction(self._raw_client, self._server, self._auth)

    @cached_property
    def feedback(self) -> AsyncFeedback:
        return AsyncFeedback(self._raw_client, self._server, self._auth)

    @cached_property
    def interact(self) -> AsyncInteract:
        return AsyncInteract(self._raw_client, self._server, self._auth)

    @cached_property
    def mapping_api(self) -> AsyncMappingApi:
        return AsyncMappingApi(self._raw_client, self._server, self._auth)

    @cached_property
    def miscellaneous(self) -> AsyncMiscellaneous:
        return AsyncMiscellaneous(self._raw_client, self._server, self._auth)

    @cached_property
    def monitoring(self) -> AsyncMonitoring:
        return AsyncMonitoring(self._raw_client, self._server, self._auth)

    @cached_property
    def research_api(self) -> AsyncResearchApi:
        return AsyncResearchApi(self._raw_client, self._server, self._auth)

    @cached_property
    def scraping(self) -> AsyncScraping:
        return AsyncScraping(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def support(self) -> AsyncSupport:
        return AsyncSupport(self._raw_client, self._server, self._auth)

    @cached_property
    def threat_protection(self) -> AsyncThreatProtection:
        return AsyncThreatProtection(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncFirecrawlApiClient
