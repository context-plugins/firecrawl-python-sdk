<!-- Generated file — do not edit; regenerated with the SDK. -->

# Miscellaneous — operations

Accessor: `client.miscellaneous` · Source: `firecrawl_api/apis/miscellaneous.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.miscellaneous.get_queue_status

- **Route**: `GET /team/queue-status`
- **Signature**: `def get_queue_status(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TeamQueueStatusResponse`
- **Returns (raw)**: `ApiResult[TeamQueueStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TeamQueueStatusResponse` | `firecrawl_api/models/team_queue_status_response.py` |

