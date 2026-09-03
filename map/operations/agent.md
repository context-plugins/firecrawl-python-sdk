<!-- Generated file — do not edit; regenerated with the SDK. -->

# Agent — operations

Accessor: `client.agent` · Source: `firecrawl_api/apis/agent.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.agent.cancel_agent

- **Route**: `DELETE /agent/{jobId}`
- **Auth**: `bearer_auth`
- **Signature**: `def cancel_agent(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`
- **Params**: `job_id` — path `jobId`
- **Returns (parsed)**: `SuccessResponse`
- **Returns (raw)**: `ApiResult[SuccessResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SuccessResponse` | `firecrawl_api/models/success_response.py` |

### client.agent.get_agent_status

- **Route**: `GET /agent/{jobId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_agent_status(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`
- **Params**: `job_id` — path `jobId`
- **Returns (parsed)**: `AgentResponse1`
- **Returns (raw)**: `ApiResult[AgentResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AgentResponse1` | `firecrawl_api/models/agent_response1.py` |

### client.agent.start_agent

- **Route**: `POST /agent`
- **Auth**: `bearer_auth`
- **Signature**: `def start_agent(body: AgentRequest | AgentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AgentResponse`
- **Returns (raw)**: `ApiResult[AgentResponse, StartAgentErrorBody]`
- **Error**: `StartAgentErrorBody` — **Case A (typed)**
- **Error arms**: `Agent402Error1` [402] · `Agent429Error1` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AgentRequest` | `firecrawl_api/models/agent_request.py` |
| `AgentRequestDict` | `firecrawl_api/models/agent_request.py` |
| `AgentResponse` | `firecrawl_api/models/agent_response.py` |
| `StartAgentErrorBody` | `firecrawl_api/errors/start_agent_error.py` |
| `Agent402Error1` | `firecrawl_api/models/agent402_error1.py` |
| `Agent429Error1` | `firecrawl_api/models/agent429_error1.py` |

