from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeveloperSearchPostErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeveloperSearchPostError:
    def map(self, response: HttpResponse) -> DeveloperSearchPostErrorBody:
        match response.status_code:
            case 400 | 401 | 429 | 500:
                return RawError(response)
            case _:
                return RawError(response)


developer_search_post_error_mapper: Final[ErrorMapper[DeveloperSearchPostErrorBody]] = _DeveloperSearchPostError()
