from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.crawl402_error1 import Crawl402Error1
from ..models.crawl429_error1 import Crawl429Error1
from ..models.crawl500_error1 import Crawl500Error1

CrawlUrlsErrorBody: TypeAlias = Crawl402Error1 | Crawl429Error1 | Crawl500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CrawlUrlsError:
    def map(self, response: HttpResponse) -> CrawlUrlsErrorBody:
        match response.status_code:
            case 402:
                return decode_json[Crawl402Error1](response)
            case 429:
                return decode_json[Crawl429Error1](response)
            case 500:
                return decode_json[Crawl500Error1](response)
            case _:
                return RawError(response)


crawl_urls_error_mapper: Final[ErrorMapper[CrawlUrlsErrorBody]] = _CrawlUrlsError()
