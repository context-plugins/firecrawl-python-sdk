<!-- Generated file — do not edit; regenerated with the SDK. -->

# ResearchApi — operations

Accessor: `client.research_api` · Source: `firecrawl/apis/research_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.research_api.research_get_paper

- **Route**: `GET /search/research/papers/{id}`
- **Signature**: `def research_get_paper(id: str, *, query: str | None = None, k: int | None = 4, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path · `query` — query · `k` — query
- **Returns (parsed)**: `SearchResearchPapersResponse`
- **Returns (raw)**: `ApiResult[SearchResearchPapersResponse, ResearchGetPaperErrorBody]`
- **Error**: `ResearchGetPaperErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `SearchResearchPapersResponse` | `firecrawl/models/unions/search_research_papers_response.py` |
| `ResearchGetPaperErrorBody` | `firecrawl/errors/research_get_paper_error.py` |

### client.research_api.research_related_papers

- **Route**: `GET /search/research/papers/{id}/similar`
- **Signature**: `def research_related_papers(id: str, intent: str, *, mode: Mode5OrStr | None = None, k: int | None = 40, rerank: bool | None = None, anchor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `intent`
- **Params**: `id` — path · `intent` — query · `mode` — query · `k` — query · `rerank` — query · `anchor` — query
- **Returns (parsed)**: `ResearchSimilarPapersResponse`
- **Returns (raw)**: `ApiResult[ResearchSimilarPapersResponse, ResearchRelatedPapersErrorBody]`
- **Error**: `ResearchRelatedPapersErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `Mode5OrStr` | `firecrawl/models/enums/mode5.py` |
| `ResearchSimilarPapersResponse` | `firecrawl/models/research_similar_papers_response.py` |
| `ResearchRelatedPapersErrorBody` | `firecrawl/errors/research_related_papers_error.py` |

### client.research_api.research_search_papers

- **Route**: `GET /search/research/papers`
- **Signature**: `def research_search_papers(query: str, *, k: int | None = 40, authors: str | None = None, categories: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query`
- **Params**: `query` — query · `k` — query · `authors` — query · `categories` — query · `from_` — query `from` · `to` — query
- **Returns (parsed)**: `ResearchSearchPapersResponse`
- **Returns (raw)**: `ApiResult[ResearchSearchPapersResponse, ResearchSearchPapersErrorBody]`
- **Error**: `ResearchSearchPapersErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `ResearchSearchPapersResponse` | `firecrawl/models/research_search_papers_response.py` |
| `ResearchSearchPapersErrorBody` | `firecrawl/errors/research_search_papers_error.py` |

