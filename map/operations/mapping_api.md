<!-- Generated file — do not edit; regenerated with the SDK. -->

# MappingApi — operations

Accessor: `client.mapping_api` · Source: `firecrawl_api/apis/mapping_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mapping_api.map_urls

- **Route**: `POST /map`
- **Auth**: `bearer_auth`
- **Signature**: `def map_urls(body: MapRequest | MapRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `MapResponse`
- **Returns (raw)**: `ApiResult[MapResponse, MapUrlsErrorBody]`
- **Error**: `MapUrlsErrorBody` — **Case A (typed)**
- **Error arms**: `Map402Error1` [402] · `Map429Error1` [429] · `Map500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MapRequest` | `firecrawl_api/models/map_request.py` |
| `MapRequestDict` | `firecrawl_api/models/map_request.py` |
| `MapResponse` | `firecrawl_api/models/map_response.py` |
| `MapUrlsErrorBody` | `firecrawl_api/errors/map_urls_error.py` |
| `Map402Error1` | `firecrawl_api/models/map402_error1.py` |
| `Map429Error1` | `firecrawl_api/models/map429_error1.py` |
| `Map500Error1` | `firecrawl_api/models/map500_error1.py` |

