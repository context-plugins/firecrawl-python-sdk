<!-- Generated file — do not edit; regenerated with the SDK. -->

# Search — operations

Accessor: `client.search` · Source: `firecrawl_api/apis/search.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search.search_and_scrape

- **Route**: `POST /search`
- **Auth**: `bearer_auth`
- **Signature**: `def search_and_scrape(body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchResponse`
- **Returns (raw)**: `ApiResult[SearchResponse, SearchAndScrapeErrorBody]`
- **Error**: `SearchAndScrapeErrorBody` — **Case A (typed)**
- **Error arms**: `Search408Error1` [408] · `Search500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SearchRequest` | `firecrawl_api/models/search_request.py` |
| `SearchRequestDict` | `firecrawl_api/models/search_request.py` |
| `SearchResponse` | `firecrawl_api/models/search_response.py` |
| `SearchAndScrapeErrorBody` | `firecrawl_api/errors/search_and_scrape_error.py` |
| `Search408Error1` | `firecrawl_api/models/search408_error1.py` |
| `Search500Error1` | `firecrawl_api/models/search500_error1.py` |

### client.search.submit_search_feedback

- **Route**: `POST /search/{jobId}/feedback`
- **Auth**: `bearer_auth`
- **Signature**: `def submit_search_feedback(job_id: UUID, body: SearchFeedbackRequest | SearchFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`, `body`
- **Params**: `job_id` — path `jobId` · `body` — JSON body
- **Returns (parsed)**: `FeedbackResponse`
- **Returns (raw)**: `ApiResult[FeedbackResponse, SubmitSearchFeedbackErrorBody]`
- **Error**: `SubmitSearchFeedbackErrorBody` — **Case A (typed)**
- **Error arms**: `FeedbackErrorResponse` [400, 403, 404, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SearchFeedbackRequest` | `firecrawl_api/models/search_feedback_request.py` |
| `SearchFeedbackRequestDict` | `firecrawl_api/models/search_feedback_request.py` |
| `FeedbackResponse` | `firecrawl_api/models/feedback_response.py` |
| `SubmitSearchFeedbackErrorBody` | `firecrawl_api/errors/submit_search_feedback_error.py` |
| `FeedbackErrorResponse` | `firecrawl_api/models/feedback_error_response.py` |

