from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.crawl404_error1 import Crawl404Error1
from ..models.crawl500_error1 import Crawl500Error1

CancelCrawlErrorBody: TypeAlias = Crawl404Error1 | Crawl500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _CancelCrawlError:
    def map(self, response: HttpResponse) -> CancelCrawlErrorBody:
        match response.status_code:
            case 404:
                return decode_json[Crawl404Error1](response)
            case 500:
                return decode_json[Crawl500Error1](response)
            case _:
                return RawError(response)


cancel_crawl_error_mapper: Final[ErrorMapper[CancelCrawlErrorBody]] = _CancelCrawlError()
