<!-- Generated file — do not edit; regenerated with the SDK. -->

# Crawling — operations

Accessor: `client.crawling` · Source: `firecrawl/apis/crawling.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.crawling.cancel_crawl

- **Route**: `DELETE /crawl/{id}`
- **Signature**: `def cancel_crawl(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `CrawlResponse1`
- **Returns (raw)**: `ApiResult[CrawlResponse1, CancelCrawlErrorBody]`
- **Error**: `CancelCrawlErrorBody` — **Case A (typed)**
- **Error arms**: `Crawl404Error1` [404] · `Crawl500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlResponse1` | `firecrawl/models/crawl_response1.py` |
| `CancelCrawlErrorBody` | `firecrawl/errors/cancel_crawl_error.py` |
| `Crawl404Error1` | `firecrawl/models/crawl404_error1.py` |
| `Crawl500Error1` | `firecrawl/models/crawl500_error1.py` |

### client.crawling.crawl_params_preview

- **Route**: `POST /crawl/params-preview`
- **Signature**: `def crawl_params_preview(body: CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CrawlParamsPreviewResponse`
- **Returns (raw)**: `ApiResult[CrawlParamsPreviewResponse, CrawlParamsPreviewErrorBody]`
- **Error**: `CrawlParamsPreviewErrorBody` — **Case A (typed)**
- **Error arms**: `CrawlParamsPreview400Error1` [400] · `CrawlParamsPreview401Error1` [401] · `CrawlParamsPreview500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlParamsPreviewRequest` | `firecrawl/models/crawl_params_preview_request.py` |
| `CrawlParamsPreviewRequestDict` | `firecrawl/models/crawl_params_preview_request.py` |
| `CrawlParamsPreviewResponse` | `firecrawl/models/crawl_params_preview_response.py` |
| `CrawlParamsPreviewErrorBody` | `firecrawl/errors/crawl_params_preview_error.py` |
| `CrawlParamsPreview400Error1` | `firecrawl/models/crawl_params_preview400_error1.py` |
| `CrawlParamsPreview401Error1` | `firecrawl/models/crawl_params_preview401_error1.py` |
| `CrawlParamsPreview500Error1` | `firecrawl/models/crawl_params_preview500_error1.py` |

### client.crawling.crawl_urls

- **Route**: `POST /crawl`
- **Signature**: `def crawl_urls(body: CrawlRequest | CrawlRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CrawlResponse`
- **Returns (raw)**: `ApiResult[CrawlResponse, CrawlUrlsErrorBody]`
- **Error**: `CrawlUrlsErrorBody` — **Case A (typed)**
- **Error arms**: `Crawl402Error1` [402] · `Crawl429Error1` [429] · `Crawl500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlRequest` | `firecrawl/models/crawl_request.py` |
| `CrawlRequestDict` | `firecrawl/models/crawl_request.py` |
| `CrawlResponse` | `firecrawl/models/crawl_response.py` |
| `CrawlUrlsErrorBody` | `firecrawl/errors/crawl_urls_error.py` |
| `Crawl402Error1` | `firecrawl/models/crawl402_error1.py` |
| `Crawl429Error1` | `firecrawl/models/crawl429_error1.py` |
| `Crawl500Error1` | `firecrawl/models/crawl500_error1.py` |

### client.crawling.get_active_crawls

- **Route**: `GET /crawl/active`
- **Signature**: `def get_active_crawls(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `CrawlActiveResponse`
- **Returns (raw)**: `ApiResult[CrawlActiveResponse, GetActiveCrawlsErrorBody]`
- **Error**: `GetActiveCrawlsErrorBody` — **Case A (typed)**
- **Error arms**: `CrawlActive402Error1` [402] · `CrawlActive429Error1` [429] · `CrawlActive500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlActiveResponse` | `firecrawl/models/crawl_active_response.py` |
| `GetActiveCrawlsErrorBody` | `firecrawl/errors/get_active_crawls_error.py` |
| `CrawlActive402Error1` | `firecrawl/models/crawl_active402_error1.py` |
| `CrawlActive429Error1` | `firecrawl/models/crawl_active429_error1.py` |
| `CrawlActive500Error1` | `firecrawl/models/crawl_active500_error1.py` |

### client.crawling.get_crawl_errors

- **Route**: `GET /crawl/{id}/errors`
- **Signature**: `def get_crawl_errors(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `CrawlErrorsResponseObj`
- **Returns (raw)**: `ApiResult[CrawlErrorsResponseObj, GetCrawlErrorsErrorBody]`
- **Error**: `GetCrawlErrorsErrorBody` — **Case A (typed)**
- **Error arms**: `CrawlErrors402Error1` [402] · `CrawlErrors429Error1` [429] · `CrawlErrors500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlErrorsResponseObj` | `firecrawl/models/crawl_errors_response_obj.py` |
| `GetCrawlErrorsErrorBody` | `firecrawl/errors/get_crawl_errors_error.py` |
| `CrawlErrors402Error1` | `firecrawl/models/crawl_errors402_error1.py` |
| `CrawlErrors429Error1` | `firecrawl/models/crawl_errors429_error1.py` |
| `CrawlErrors500Error1` | `firecrawl/models/crawl_errors500_error1.py` |

### client.crawling.get_crawl_status

- **Route**: `GET /crawl/{id}`
- **Signature**: `def get_crawl_status(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `CrawlStatusResponseObj`
- **Returns (raw)**: `ApiResult[CrawlStatusResponseObj, GetCrawlStatusErrorBody]`
- **Error**: `GetCrawlStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Crawl402Error1` [402] · `Crawl429Error1` [429] · `Crawl500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlStatusResponseObj` | `firecrawl/models/crawl_status_response_obj.py` |
| `GetCrawlStatusErrorBody` | `firecrawl/errors/get_crawl_status_error.py` |
| `Crawl402Error1` | `firecrawl/models/crawl402_error1.py` |
| `Crawl429Error1` | `firecrawl/models/crawl429_error1.py` |
| `Crawl500Error1` | `firecrawl/models/crawl500_error1.py` |

