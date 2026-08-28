<!-- Generated file — do not edit; regenerated with the SDK. -->

# Support — operations

Accessor: `client.support` · Source: `firecrawl/apis/support.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.support.ask_support_agent

- **Route**: `POST /support/ask`
- **Signature**: `def ask_support_agent(body: SupportAskRequest | SupportAskRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SupportAskResponse`
- **Returns (raw)**: `ApiResult[SupportAskResponse, AskSupportAgentErrorBody]`
- **Error**: `AskSupportAgentErrorBody` — **Case A (typed)**
- **Error arms**: `SupportProxyErrorResponse` [400, 401, 503, 504] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SupportAskRequest` | `firecrawl/models/support_ask_request.py` |
| `SupportAskRequestDict` | `firecrawl/models/support_ask_request.py` |
| `SupportAskResponse` | `firecrawl/models/support_ask_response.py` |
| `AskSupportAgentErrorBody` | `firecrawl/errors/ask_support_agent_error.py` |
| `SupportProxyErrorResponse` | `firecrawl/models/support_proxy_error_response.py` |

### client.support.search_support_docs

- **Route**: `POST /support/docs-search`
- **Signature**: `def search_support_docs(body: SupportDocsSearchRequest | SupportDocsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SupportDocsSearchResponse`
- **Returns (raw)**: `ApiResult[SupportDocsSearchResponse, SearchSupportDocsErrorBody]`
- **Error**: `SearchSupportDocsErrorBody` — **Case A (typed)**
- **Error arms**: `SupportProxyErrorResponse` [400, 401, 503, 504] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SupportDocsSearchRequest` | `firecrawl/models/support_docs_search_request.py` |
| `SupportDocsSearchRequestDict` | `firecrawl/models/support_docs_search_request.py` |
| `SupportDocsSearchResponse` | `firecrawl/models/support_docs_search_response.py` |
| `SearchSupportDocsErrorBody` | `firecrawl/errors/search_support_docs_error.py` |
| `SupportProxyErrorResponse` | `firecrawl/models/support_proxy_error_response.py` |

