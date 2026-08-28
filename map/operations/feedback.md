<!-- Generated file — do not edit; regenerated with the SDK. -->

# Feedback — operations

Accessor: `client.feedback` · Source: `firecrawl/apis/feedback.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.feedback.submit_endpoint_feedback

- **Route**: `POST /feedback`
- **Signature**: `def submit_endpoint_feedback(body: EndpointFeedbackRequest | EndpointFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FeedbackResponse`
- **Returns (raw)**: `ApiResult[FeedbackResponse, SubmitEndpointFeedbackErrorBody]`
- **Error**: `SubmitEndpointFeedbackErrorBody` — **Case A (typed)**
- **Error arms**: `FeedbackErrorResponse` [400, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EndpointFeedbackRequest` | `firecrawl/models/endpoint_feedback_request.py` |
| `EndpointFeedbackRequestDict` | `firecrawl/models/endpoint_feedback_request.py` |
| `FeedbackResponse` | `firecrawl/models/feedback_response.py` |
| `SubmitEndpointFeedbackErrorBody` | `firecrawl/errors/submit_endpoint_feedback_error.py` |
| `FeedbackErrorResponse` | `firecrawl/models/feedback_error_response.py` |

### client.feedback.submit_search_feedback

- **Route**: `POST /search/{jobId}/feedback`
- **Signature**: `def submit_search_feedback(job_id: UUID, body: SearchFeedbackRequest | SearchFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`, `body`
- **Params**: `job_id` — path `jobId` · `body` — JSON body
- **Returns (parsed)**: `FeedbackResponse`
- **Returns (raw)**: `ApiResult[FeedbackResponse, SubmitSearchFeedbackErrorBody]`
- **Error**: `SubmitSearchFeedbackErrorBody` — **Case A (typed)**
- **Error arms**: `FeedbackErrorResponse` [400, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SearchFeedbackRequest` | `firecrawl/models/search_feedback_request.py` |
| `SearchFeedbackRequestDict` | `firecrawl/models/search_feedback_request.py` |
| `FeedbackResponse` | `firecrawl/models/feedback_response.py` |
| `SubmitSearchFeedbackErrorBody` | `firecrawl/errors/submit_search_feedback_error.py` |
| `FeedbackErrorResponse` | `firecrawl/models/feedback_error_response.py` |

