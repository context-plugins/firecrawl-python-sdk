from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.feedback_error_response import FeedbackErrorResponse

SubmitEndpointFeedbackErrorBody: TypeAlias = FeedbackErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _SubmitEndpointFeedbackError:
    def map(self, response: HttpResponse) -> SubmitEndpointFeedbackErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 409 | 500:
                return decode_json[FeedbackErrorResponse](response)
            case _:
                return RawError(response)


submit_endpoint_feedback_error_mapper: Final[
    ErrorMapper[SubmitEndpointFeedbackErrorBody]
] = _SubmitEndpointFeedbackError()
