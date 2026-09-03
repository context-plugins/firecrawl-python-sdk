<!-- Generated file — do not edit; regenerated with the SDK. -->

# Extraction — operations

Accessor: `client.extraction` · Source: `firecrawl_api/apis/extraction.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.extraction.extract_data

- **Route**: `POST /extract`
- **Auth**: `bearer_auth`
- **Signature**: `def extract_data(body: ExtractRequest | ExtractRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ExtractResponse`
- **Returns (raw)**: `ApiResult[ExtractResponse, ExtractDataErrorBody]`
- **Error**: `ExtractDataErrorBody` — **Case A (typed)**
- **Error arms**: `Extract400Error1` [400] · `Extract500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ExtractRequest` | `firecrawl_api/models/extract_request.py` |
| `ExtractRequestDict` | `firecrawl_api/models/extract_request.py` |
| `ExtractResponse` | `firecrawl_api/models/extract_response.py` |
| `ExtractDataErrorBody` | `firecrawl_api/errors/extract_data_error.py` |
| `Extract400Error1` | `firecrawl_api/models/extract400_error1.py` |
| `Extract500Error1` | `firecrawl_api/models/extract500_error1.py` |

### client.extraction.get_extract_status

- **Route**: `GET /extract/{id}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_extract_status(id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `ExtractStatusResponse`
- **Returns (raw)**: `ApiResult[ExtractStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ExtractStatusResponse` | `firecrawl_api/models/extract_status_response.py` |

