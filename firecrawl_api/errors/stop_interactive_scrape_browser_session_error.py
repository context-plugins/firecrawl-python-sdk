from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.scrape_interact403_error1 import ScrapeInteract403Error1
from ..models.scrape_interact404_error1 import ScrapeInteract404Error1

StopInteractiveScrapeBrowserSessionErrorBody: TypeAlias = ScrapeInteract403Error1 | ScrapeInteract404Error1 | RawError


@dataclass(frozen=True, slots=True)
class _StopInteractiveScrapeBrowserSessionError:
    def map(self, response: HttpResponse) -> StopInteractiveScrapeBrowserSessionErrorBody:
        match response.status_code:
            case 403:
                return decode_json[ScrapeInteract403Error1](response)
            case 404:
                return decode_json[ScrapeInteract404Error1](response)
            case _:
                return RawError(response)


stop_interactive_scrape_browser_session_error_mapper: Final[
    ErrorMapper[StopInteractiveScrapeBrowserSessionErrorBody]
] = _StopInteractiveScrapeBrowserSessionError()
