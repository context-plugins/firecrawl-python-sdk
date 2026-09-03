from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.scrape_interact400_error1 import ScrapeInteract400Error1
from ..models.scrape_interact402_error1 import ScrapeInteract402Error1
from ..models.scrape_interact403_error1 import ScrapeInteract403Error1
from ..models.scrape_interact404_error1 import ScrapeInteract404Error1
from ..models.scrape_interact409_error1 import ScrapeInteract409Error1
from ..models.scrape_interact410_error1 import ScrapeInteract410Error1
from ..models.scrape_interact429_error1 import ScrapeInteract429Error1
from ..models.scrape_interact502_error1 import ScrapeInteract502Error1

InteractWithScrapeBrowserSessionErrorBody: TypeAlias = (
    ScrapeInteract400Error1
    | ScrapeInteract402Error1
    | ScrapeInteract403Error1
    | ScrapeInteract404Error1
    | ScrapeInteract409Error1
    | ScrapeInteract410Error1
    | ScrapeInteract429Error1
    | ScrapeInteract502Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _InteractWithScrapeBrowserSessionError:
    def map(self, response: HttpResponse) -> InteractWithScrapeBrowserSessionErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ScrapeInteract400Error1](response)
            case 402:
                return decode_json[ScrapeInteract402Error1](response)
            case 403:
                return decode_json[ScrapeInteract403Error1](response)
            case 404:
                return decode_json[ScrapeInteract404Error1](response)
            case 409:
                return decode_json[ScrapeInteract409Error1](response)
            case 410:
                return decode_json[ScrapeInteract410Error1](response)
            case 429:
                return decode_json[ScrapeInteract429Error1](response)
            case 502:
                return decode_json[ScrapeInteract502Error1](response)
            case _:
                return RawError(response)


interact_with_scrape_browser_session_error_mapper: Final[
    ErrorMapper[InteractWithScrapeBrowserSessionErrorBody]
] = _InteractWithScrapeBrowserSessionError()
