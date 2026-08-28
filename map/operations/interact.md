<!-- Generated file — do not edit; regenerated with the SDK. -->

# Interact — operations

Accessor: `client.interact` · Source: `firecrawl/apis/interact.py` · 4 operations

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
| `InteractRequest` | `firecrawl/models/interact_request.py` |
| `InteractRequestDict` | `firecrawl/models/interact_request.py` |
| `InteractResponse` | `firecrawl/models/interact_response.py` |
| `CreateBrowserSessionErrorBody` | `firecrawl/errors/create_browser_session_error.py` |
| `Interact402Error1` | `firecrawl/models/interact402_error1.py` |

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
| `InteractResponse2` | `firecrawl/models/interact_response2.py` |
| `DeleteBrowserSessionErrorBody` | `firecrawl/errors/delete_browser_session_error.py` |
| `Interact402Error1` | `firecrawl/models/interact402_error1.py` |

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
| `InteractExecuteRequest` | `firecrawl/models/interact_execute_request.py` |
| `InteractExecuteRequestDict` | `firecrawl/models/interact_execute_request.py` |
| `InteractExecuteResponse` | `firecrawl/models/interact_execute_response.py` |
| `ExecuteBrowserCodeErrorBody` | `firecrawl/errors/execute_browser_code_error.py` |
| `InteractExecute402Error1` | `firecrawl/models/interact_execute402_error1.py` |

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
| `Status10OrStr` | `firecrawl/models/enums/status10.py` |
| `InteractResponse1` | `firecrawl/models/interact_response1.py` |
| `ListBrowserSessionsErrorBody` | `firecrawl/errors/list_browser_sessions_error.py` |
| `Interact402Error1` | `firecrawl/models/interact402_error1.py` |

