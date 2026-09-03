<!-- Generated file — do not edit; regenerated with the SDK. -->

# ThreatProtection — operations

Accessor: `client.threat_protection` · Source: `firecrawl_api/apis/threat_protection.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.threat_protection.get_threat_protection

- **Route**: `GET /team/threat-protection`
- **Auth**: `bearer_auth`
- **Signature**: `def get_threat_protection(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TeamThreatProtectionResponse`
- **Returns (raw)**: `ApiResult[TeamThreatProtectionResponse, GetThreatProtectionErrorBody]`
- **Error**: `GetThreatProtectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [403, anything unmapped]

| Type | Source |
| --- | --- |
| `TeamThreatProtectionResponse` | `firecrawl_api/models/team_threat_protection_response.py` |
| `GetThreatProtectionErrorBody` | `firecrawl_api/errors/get_threat_protection_error.py` |

### client.threat_protection.update_threat_protection

- **Route**: `PUT /team/threat-protection`
- **Auth**: `bearer_auth`
- **Signature**: `def update_threat_protection(body: TeamThreatProtectionRequest | TeamThreatProtectionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TeamThreatProtectionResponse`
- **Returns (raw)**: `ApiResult[TeamThreatProtectionResponse, UpdateThreatProtectionErrorBody]`
- **Error**: `UpdateThreatProtectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, anything unmapped]

| Type | Source |
| --- | --- |
| `TeamThreatProtectionRequest` | `firecrawl_api/models/team_threat_protection_request.py` |
| `TeamThreatProtectionRequestDict` | `firecrawl_api/models/team_threat_protection_request.py` |
| `TeamThreatProtectionResponse` | `firecrawl_api/models/team_threat_protection_response.py` |
| `UpdateThreatProtectionErrorBody` | `firecrawl_api/errors/update_threat_protection_error.py` |

