<!-- Generated file — do not edit; regenerated with the SDK. -->

# Scraping — operations

Accessor: `client.scraping` · Source: `firecrawl_api/apis/scraping.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.scraping.cancel_batch_scrape

- **Route**: `DELETE /batch/scrape/{id}`
- **Signature**: `def cancel_batch_scrape(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `BatchScrapeResponse`
- **Returns (raw)**: `ApiResult[BatchScrapeResponse, CancelBatchScrapeErrorBody]`
- **Error**: `CancelBatchScrapeErrorBody` — **Case A (typed)**
- **Error arms**: `BatchScrape404Error1` [404] · `BatchScrape500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BatchScrapeResponse` | `firecrawl_api/models/batch_scrape_response.py` |
| `CancelBatchScrapeErrorBody` | `firecrawl_api/errors/cancel_batch_scrape_error.py` |
| `BatchScrape404Error1` | `firecrawl_api/models/batch_scrape404_error1.py` |
| `BatchScrape500Error1` | `firecrawl_api/models/batch_scrape500_error1.py` |

### client.scraping.get_batch_scrape_errors

- **Route**: `GET /batch/scrape/{id}/errors`
- **Signature**: `def get_batch_scrape_errors(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `CrawlErrorsResponseObj`
- **Returns (raw)**: `ApiResult[CrawlErrorsResponseObj, GetBatchScrapeErrorsErrorBody]`
- **Error**: `GetBatchScrapeErrorsErrorBody` — **Case A (typed)**
- **Error arms**: `BatchScrapeErrors402Error1` [402] · `BatchScrapeErrors429Error1` [429] · `BatchScrapeErrors500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CrawlErrorsResponseObj` | `firecrawl_api/models/crawl_errors_response_obj.py` |
| `GetBatchScrapeErrorsErrorBody` | `firecrawl_api/errors/get_batch_scrape_errors_error.py` |
| `BatchScrapeErrors402Error1` | `firecrawl_api/models/batch_scrape_errors402_error1.py` |
| `BatchScrapeErrors429Error1` | `firecrawl_api/models/batch_scrape_errors429_error1.py` |
| `BatchScrapeErrors500Error1` | `firecrawl_api/models/batch_scrape_errors500_error1.py` |

### client.scraping.get_batch_scrape_status

- **Route**: `GET /batch/scrape/{id}`
- **Signature**: `def get_batch_scrape_status(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `BatchScrapeStatusResponseObj`
- **Returns (raw)**: `ApiResult[BatchScrapeStatusResponseObj, GetBatchScrapeStatusErrorBody]`
- **Error**: `GetBatchScrapeStatusErrorBody` — **Case A (typed)**
- **Error arms**: `BatchScrape402Error1` [402] · `BatchScrape429Error1` [429] · `BatchScrape500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BatchScrapeStatusResponseObj` | `firecrawl_api/models/batch_scrape_status_response_obj.py` |
| `GetBatchScrapeStatusErrorBody` | `firecrawl_api/errors/get_batch_scrape_status_error.py` |
| `BatchScrape402Error1` | `firecrawl_api/models/batch_scrape402_error1.py` |
| `BatchScrape429Error1` | `firecrawl_api/models/batch_scrape429_error1.py` |
| `BatchScrape500Error1` | `firecrawl_api/models/batch_scrape500_error1.py` |

### client.scraping.get_scrape_status

- **Route**: `GET /scrape/{jobId}`
- **Signature**: `def get_scrape_status(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`
- **Params**: `job_id` — path `jobId`
- **Returns (parsed)**: `ScrapeResponse`
- **Returns (raw)**: `ApiResult[ScrapeResponse, GetScrapeStatusErrorBody]`
- **Error**: `GetScrapeStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Scrape402Error21` [402] · `Scrape429Error21` [429] · `Scrape500Error21` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScrapeResponse` | `firecrawl_api/models/scrape_response.py` |
| `GetScrapeStatusErrorBody` | `firecrawl_api/errors/get_scrape_status_error.py` |
| `Scrape402Error21` | `firecrawl_api/models/scrape402_error21.py` |
| `Scrape429Error21` | `firecrawl_api/models/scrape429_error21.py` |
| `Scrape500Error21` | `firecrawl_api/models/scrape500_error21.py` |

### client.scraping.interact_with_scrape_browser_session

- **Route**: `POST /scrape/{jobId}/interact`
- **Signature**: `def interact_with_scrape_browser_session(job_id: UUID, body: ScrapeInteractRequest | ScrapeInteractRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`, `body`
- **Params**: `job_id` — path `jobId` · `body` — JSON body
- **Returns (parsed)**: `ScrapeInteractResponse`
- **Returns (raw)**: `ApiResult[ScrapeInteractResponse, InteractWithScrapeBrowserSessionErrorBody]`
- **Error**: `InteractWithScrapeBrowserSessionErrorBody` — **Case A (typed)**
- **Error arms**: `ScrapeInteract400Error1` [400] · `ScrapeInteract402Error1` [402] · `ScrapeInteract403Error1` [403] · `ScrapeInteract404Error1` [404] · `ScrapeInteract409Error1` [409] · `ScrapeInteract410Error1` [410] · `ScrapeInteract429Error1` [429] · `ScrapeInteract502Error1` [502] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScrapeInteractRequest` | `firecrawl_api/models/scrape_interact_request.py` |
| `ScrapeInteractRequestDict` | `firecrawl_api/models/scrape_interact_request.py` |
| `ScrapeInteractResponse` | `firecrawl_api/models/scrape_interact_response.py` |
| `InteractWithScrapeBrowserSessionErrorBody` | `firecrawl_api/errors/interact_with_scrape_browser_session_error.py` |
| `ScrapeInteract400Error1` | `firecrawl_api/models/scrape_interact400_error1.py` |
| `ScrapeInteract402Error1` | `firecrawl_api/models/scrape_interact402_error1.py` |
| `ScrapeInteract403Error1` | `firecrawl_api/models/scrape_interact403_error1.py` |
| `ScrapeInteract404Error1` | `firecrawl_api/models/scrape_interact404_error1.py` |
| `ScrapeInteract409Error1` | `firecrawl_api/models/scrape_interact409_error1.py` |
| `ScrapeInteract410Error1` | `firecrawl_api/models/scrape_interact410_error1.py` |
| `ScrapeInteract429Error1` | `firecrawl_api/models/scrape_interact429_error1.py` |
| `ScrapeInteract502Error1` | `firecrawl_api/models/scrape_interact502_error1.py` |

### client.scraping.parse_file

- **Route**: `POST /parse`
- **Signature**: `def parse_file(file: bytes, *, options: ParseOptions | ParseOptionsDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file`
- **Params**: `options` — multipart field · `file` — multipart file
- **Returns (parsed)**: `ScrapeResponse`
- **Returns (raw)**: `ApiResult[ScrapeResponse, ParseFileErrorBody]`
- **Error**: `ParseFileErrorBody` — **Case A (typed)**
- **Error arms**: `Parse400Error1` [400] · `Parse402Error1` [402] · `Parse429Error1` [429] · `Parse500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ParseOptions` | `firecrawl_api/models/parse_options.py` |
| `ParseOptionsDict` | `firecrawl_api/models/parse_options.py` |
| `ScrapeResponse` | `firecrawl_api/models/scrape_response.py` |
| `ParseFileErrorBody` | `firecrawl_api/errors/parse_file_error.py` |
| `Parse400Error1` | `firecrawl_api/models/parse400_error1.py` |
| `Parse402Error1` | `firecrawl_api/models/parse402_error1.py` |
| `Parse429Error1` | `firecrawl_api/models/parse429_error1.py` |
| `Parse500Error1` | `firecrawl_api/models/parse500_error1.py` |

### client.scraping.scrape_and_extract_from_url

- **Route**: `POST /scrape`
- **Signature**: `def scrape_and_extract_from_url(body: ScrapeRequest | ScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ScrapeResponse`
- **Returns (raw)**: `ApiResult[ScrapeResponse, ScrapeAndExtractFromUrlErrorBody]`
- **Error**: `ScrapeAndExtractFromUrlErrorBody` — **Case A (typed)**
- **Error arms**: `Scrape402Error1` [402] · `Scrape429Error1` [429] · `Scrape500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScrapeRequest` | `firecrawl_api/models/scrape_request.py` |
| `ScrapeRequestDict` | `firecrawl_api/models/scrape_request.py` |
| `ScrapeResponse` | `firecrawl_api/models/scrape_response.py` |
| `ScrapeAndExtractFromUrlErrorBody` | `firecrawl_api/errors/scrape_and_extract_from_url_error.py` |
| `Scrape402Error1` | `firecrawl_api/models/scrape402_error1.py` |
| `Scrape429Error1` | `firecrawl_api/models/scrape429_error1.py` |
| `Scrape500Error1` | `firecrawl_api/models/scrape500_error1.py` |

### client.scraping.scrape_and_extract_from_urls

- **Route**: `POST /batch/scrape`
- **Signature**: `def scrape_and_extract_from_urls(body: BatchScrapeRequest | BatchScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchScrapeResponseObj`
- **Returns (raw)**: `ApiResult[BatchScrapeResponseObj, ScrapeAndExtractFromUrlsErrorBody]`
- **Error**: `ScrapeAndExtractFromUrlsErrorBody` — **Case A (typed)**
- **Error arms**: `BatchScrape402Error1` [402] · `BatchScrape429Error1` [429] · `BatchScrape500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BatchScrapeRequest` | `firecrawl_api/models/batch_scrape_request.py` |
| `BatchScrapeRequestDict` | `firecrawl_api/models/batch_scrape_request.py` |
| `BatchScrapeResponseObj` | `firecrawl_api/models/batch_scrape_response_obj.py` |
| `ScrapeAndExtractFromUrlsErrorBody` | `firecrawl_api/errors/scrape_and_extract_from_urls_error.py` |
| `BatchScrape402Error1` | `firecrawl_api/models/batch_scrape402_error1.py` |
| `BatchScrape429Error1` | `firecrawl_api/models/batch_scrape429_error1.py` |
| `BatchScrape500Error1` | `firecrawl_api/models/batch_scrape500_error1.py` |

### client.scraping.stop_interactive_scrape_browser_session

- **Route**: `DELETE /scrape/{jobId}/interact`
- **Signature**: `def stop_interactive_scrape_browser_session(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`
- **Params**: `job_id` — path `jobId`
- **Returns (parsed)**: `SuccessResponse`
- **Returns (raw)**: `ApiResult[SuccessResponse, StopInteractiveScrapeBrowserSessionErrorBody]`
- **Error**: `StopInteractiveScrapeBrowserSessionErrorBody` — **Case A (typed)**
- **Error arms**: `ScrapeInteract403Error1` [403] · `ScrapeInteract404Error1` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SuccessResponse` | `firecrawl_api/models/success_response.py` |
| `StopInteractiveScrapeBrowserSessionErrorBody` | `firecrawl_api/errors/stop_interactive_scrape_browser_session_error.py` |
| `ScrapeInteract403Error1` | `firecrawl_api/models/scrape_interact403_error1.py` |
| `ScrapeInteract404Error1` | `firecrawl_api/models/scrape_interact404_error1.py` |

