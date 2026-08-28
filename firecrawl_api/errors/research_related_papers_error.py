from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ResearchRelatedPapersErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ResearchRelatedPapersError:
    def map(self, response: HttpResponse) -> ResearchRelatedPapersErrorBody:
        match response.status_code:
            case 400 | 401 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


research_related_papers_error_mapper: Final[ErrorMapper[ResearchRelatedPapersErrorBody]] = _ResearchRelatedPapersError()
