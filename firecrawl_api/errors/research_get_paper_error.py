from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ResearchGetPaperErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ResearchGetPaperError:
    def map(self, response: HttpResponse) -> ResearchGetPaperErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


research_get_paper_error_mapper: Final[ErrorMapper[ResearchGetPaperErrorBody]] = _ResearchGetPaperError()
