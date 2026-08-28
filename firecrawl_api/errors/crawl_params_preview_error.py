from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.crawl_params_preview400_error1 import CrawlParamsPreview400Error1
from ..models.crawl_params_preview401_error1 import CrawlParamsPreview401Error1
from ..models.crawl_params_preview500_error1 import CrawlParamsPreview500Error1

CrawlParamsPreviewErrorBody: TypeAlias = (
    CrawlParamsPreview400Error1 | CrawlParamsPreview401Error1 | CrawlParamsPreview500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _CrawlParamsPreviewError:
    def map(self, response: HttpResponse) -> CrawlParamsPreviewErrorBody:
        match response.status_code:
            case 400:
                return decode_json[CrawlParamsPreview400Error1](response)
            case 401:
                return decode_json[CrawlParamsPreview401Error1](response)
            case 500:
                return decode_json[CrawlParamsPreview500Error1](response)
            case _:
                return RawError(response)


crawl_params_preview_error_mapper: Final[ErrorMapper[CrawlParamsPreviewErrorBody]] = _CrawlParamsPreviewError()
