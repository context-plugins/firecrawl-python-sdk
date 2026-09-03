from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account import Account
from .apis.agent import Agent
from .apis.billing import Billing
from .apis.crawling import Crawling
from .apis.developer import Developer
from .apis.extraction import Extraction
from .apis.feedback import Feedback
from .apis.interact import Interact
from .apis.mapping_api import MappingApi
from .apis.miscellaneous import Miscellaneous
from .apis.monitoring import Monitoring
from .apis.research_api import ResearchApi
from .apis.scraping import Scraping
from .apis.search import Search
from .apis.support import Support
from .apis.threat_protection import ThreatProtection
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseFirecrawlApiClient
from .core import OPERATING_SYSTEM, PYTHON_RUNTIME, BearerAuthScheme, HttpClient, HttpxClient, RawClient, no_auth, param


class FirecrawlApiClient(BaseFirecrawlApiClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        bearer_auth: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "FirecrawlApiClient/v2 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "v2"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth)

    @cached_property
    def account(self) -> Account:
        return Account(self._raw_client, self._server, self._auth)

    @cached_property
    def agent(self) -> Agent:
        return Agent(self._raw_client, self._server, self._auth)

    @cached_property
    def billing(self) -> Billing:
        return Billing(self._raw_client, self._server, self._auth)

    @cached_property
    def crawling(self) -> Crawling:
        return Crawling(self._raw_client, self._server, self._auth)

    @cached_property
    def developer(self) -> Developer:
        return Developer(self._raw_client, self._server, self._auth)

    @cached_property
    def extraction(self) -> Extraction:
        return Extraction(self._raw_client, self._server, self._auth)

    @cached_property
    def feedback(self) -> Feedback:
        return Feedback(self._raw_client, self._server, self._auth)

    @cached_property
    def interact(self) -> Interact:
        return Interact(self._raw_client, self._server, self._auth)

    @cached_property
    def mapping_api(self) -> MappingApi:
        return MappingApi(self._raw_client, self._server, self._auth)

    @cached_property
    def miscellaneous(self) -> Miscellaneous:
        return Miscellaneous(self._raw_client, self._server, self._auth)

    @cached_property
    def monitoring(self) -> Monitoring:
        return Monitoring(self._raw_client, self._server, self._auth)

    @cached_property
    def research_api(self) -> ResearchApi:
        return ResearchApi(self._raw_client, self._server, self._auth)

    @cached_property
    def scraping(self) -> Scraping:
        return Scraping(self._raw_client, self._server, self._auth)

    @cached_property
    def search(self) -> Search:
        return Search(self._raw_client, self._server, self._auth)

    @cached_property
    def support(self) -> Support:
        return Support(self._raw_client, self._server, self._auth)

    @cached_property
    def threat_protection(self) -> ThreatProtection:
        return ThreatProtection(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = FirecrawlApiClient
