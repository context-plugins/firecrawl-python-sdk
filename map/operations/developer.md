<!-- Generated file — do not edit; regenerated with the SDK. -->

# Developer — operations

Accessor: `client.developer` · Source: `firecrawl_api/apis/developer.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.developer.developer_search

- **Route**: `GET /search/developer`
- **Signature**: `def developer_search(query: str, *, k: int | None = 10, types: list[Types1OrStr] | None = None, repos: list[str] | None = None, sources: list[str] | None = None, skills: SkillsOrStr | None = None, passages: int | None = 1, language: str | None = None, topic: str | None = None, license: str | None = None, min_stars: int | None = None, max_stars: int | None = None, archived: bool | None = None, fork: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query`
- **Params**: `query` — query · `k` — query · `types` — query · `repos` — query · `sources` — query · `skills` — query · `passages` — query · `language` — query · `topic` — query · `license` — query · `min_stars` — query · `max_stars` — query · `archived` — query · `fork` — query
- **Returns (parsed)**: `DeveloperSearchResponse`
- **Returns (raw)**: `ApiResult[DeveloperSearchResponse, DeveloperSearchErrorBody]`
- **Error**: `DeveloperSearchErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `Types1OrStr` | `firecrawl_api/models/enums/types1.py` |
| `SkillsOrStr` | `firecrawl_api/models/enums/skills.py` |
| `DeveloperSearchResponse` | `firecrawl_api/models/developer_search_response.py` |
| `DeveloperSearchErrorBody` | `firecrawl_api/errors/developer_search_error.py` |

### client.developer.developer_search_post

- **Route**: `POST /search/developer`
- **Signature**: `def developer_search_post(body: SearchDeveloperRequest | SearchDeveloperRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeveloperSearchResponse`
- **Returns (raw)**: `ApiResult[DeveloperSearchResponse, DeveloperSearchPostErrorBody]`
- **Error**: `DeveloperSearchPostErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `SearchDeveloperRequest` | `firecrawl_api/models/search_developer_request.py` |
| `SearchDeveloperRequestDict` | `firecrawl_api/models/search_developer_request.py` |
| `DeveloperSearchResponse` | `firecrawl_api/models/developer_search_response.py` |
| `DeveloperSearchPostErrorBody` | `firecrawl_api/errors/developer_search_post_error.py` |

