<!-- Generated file — do not edit; regenerated with the SDK. -->

# Interact — operations

Accessor: `client.interact` · Source: `firecrawl_api/apis/interact.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.interact.create_browser_session

- **Route**: `POST /interact`
- **Signature**: `def create_browser_session(body: InteractRequest | InteractRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InteractResponse`
- **Returns (raw)**: `ApiResult[InteractResponse, CreateBrowserSessionErrorBody]`
- **Error**: `CreateBrowserSessionErrorBody` — **Case A (typed)**
- **Error arms**: `Interact402Error1` [402] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InteractRequest` | `firecrawl_api/models/interact_request.py` |
| `InteractRequestDict` | `firecrawl_api/models/interact_request.py` |
| `InteractResponse` | `firecrawl_api/models/interact_response.py` |
| `CreateBrowserSessionErrorBody` | `firecrawl_api/errors/create_browser_session_error.py` |
| `Interact402Error1` | `firecrawl_api/models/interact402_error1.py` |

### client.interact.delete_browser_session

- **Route**: `DELETE /interact/{sessionId}`
- **Signature**: `def delete_browser_session(session_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `session_id`
- **Params**: `session_id` — path `sessionId`
- **Returns (parsed)**: `InteractResponse2`
- **Returns (raw)**: `ApiResult[InteractResponse2, DeleteBrowserSessionErrorBody]`
- **Error**: `DeleteBrowserSessionErrorBody` — **Case A (typed)**
- **Error arms**: `Interact402Error1` [402] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InteractResponse2` | `firecrawl_api/models/interact_response2.py` |
| `DeleteBrowserSessionErrorBody` | `firecrawl_api/errors/delete_browser_session_error.py` |
| `Interact402Error1` | `firecrawl_api/models/interact402_error1.py` |

### client.interact.execute_browser_code

- **Route**: `POST /interact/{sessionId}/execute`
- **Signature**: `def execute_browser_code(session_id: str, body: InteractExecuteRequest | InteractExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `session_id`, `body`
- **Params**: `session_id` — path `sessionId` · `body` — JSON body
- **Returns (parsed)**: `InteractExecuteResponse`
- **Returns (raw)**: `ApiResult[InteractExecuteResponse, ExecuteBrowserCodeErrorBody]`
- **Error**: `ExecuteBrowserCodeErrorBody` — **Case A (typed)**
- **Error arms**: `InteractExecute402Error1` [402] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InteractExecuteRequest` | `firecrawl_api/models/interact_execute_request.py` |
| `InteractExecuteRequestDict` | `firecrawl_api/models/interact_execute_request.py` |
| `InteractExecuteResponse` | `firecrawl_api/models/interact_execute_response.py` |
| `ExecuteBrowserCodeErrorBody` | `firecrawl_api/errors/execute_browser_code_error.py` |
| `InteractExecute402Error1` | `firecrawl_api/models/interact_execute402_error1.py` |

### client.interact.list_browser_sessions

- **Route**: `GET /interact`
- **Signature**: `def list_browser_sessions(*, status: Status10OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `status` — query
- **Returns (parsed)**: `InteractResponse1`
- **Returns (raw)**: `ApiResult[InteractResponse1, ListBrowserSessionsErrorBody]`
- **Error**: `ListBrowserSessionsErrorBody` — **Case A (typed)**
- **Error arms**: `Interact402Error1` [402] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Status10OrStr` | `firecrawl_api/models/enums/status10.py` |
| `InteractResponse1` | `firecrawl_api/models/interact_response1.py` |
| `ListBrowserSessionsErrorBody` | `firecrawl_api/errors/list_browser_sessions_error.py` |
| `Interact402Error1` | `firecrawl_api/models/interact402_error1.py` |

