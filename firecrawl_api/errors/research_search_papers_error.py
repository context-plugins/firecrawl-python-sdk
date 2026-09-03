from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ResearchSearchPapersErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ResearchSearchPapersError:
    def map(self, response: HttpResponse) -> ResearchSearchPapersErrorBody:
        match response.status_code:
            case 400 | 401 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


research_search_papers_error_mapper: Final[ErrorMapper[ResearchSearchPapersErrorBody]] = _ResearchSearchPapersError()
