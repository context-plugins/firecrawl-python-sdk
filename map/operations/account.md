<!-- Generated file — do not edit; regenerated with the SDK. -->

# Account — operations

Accessor: `client.account` · Source: `firecrawl_api/apis/account.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account.get_activity

- **Route**: `GET /team/activity`
- **Signature**: `def get_activity(*, endpoint: Endpoint1OrStr | None = None, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `endpoint` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `TeamActivityResponse`
- **Returns (raw)**: `ApiResult[TeamActivityResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Endpoint1OrStr` | `firecrawl_api/models/enums/endpoint1.py` |
| `TeamActivityResponse` | `firecrawl_api/models/team_activity_response.py` |

