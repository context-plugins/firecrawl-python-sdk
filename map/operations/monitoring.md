<!-- Generated file — do not edit; regenerated with the SDK. -->

# Monitoring — operations

Accessor: `client.monitoring` · Source: `firecrawl/apis/monitoring.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.monitoring.create_monitor

- **Route**: `POST /monitor`
- **Signature**: `def create_monitor(body: MonitorCreateRequest | MonitorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `MonitorResponse`
- **Returns (raw)**: `ApiResult[MonitorResponse, CreateMonitorErrorBody]`
- **Error**: `CreateMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `MonitorCreateRequest` | `firecrawl/models/monitor_create_request.py` |
| `MonitorCreateRequestDict` | `firecrawl/models/monitor_create_request.py` |
| `MonitorResponse` | `firecrawl/models/monitor_response.py` |
| `CreateMonitorErrorBody` | `firecrawl/errors/create_monitor_error.py` |

### client.monitoring.delete_monitor

- **Route**: `DELETE /monitor/{monitorId}`
- **Signature**: `def delete_monitor(monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path `monitorId`
- **Returns (parsed)**: `SuccessResponse`
- **Returns (raw)**: `ApiResult[SuccessResponse, DeleteMonitorErrorBody]`
- **Error**: `DeleteMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `SuccessResponse` | `firecrawl/models/success_response.py` |
| `DeleteMonitorErrorBody` | `firecrawl/errors/delete_monitor_error.py` |

### client.monitoring.get_monitor

- **Route**: `GET /monitor/{monitorId}`
- **Signature**: `def get_monitor(monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path `monitorId`
- **Returns (parsed)**: `MonitorResponse`
- **Returns (raw)**: `ApiResult[MonitorResponse, GetMonitorErrorBody]`
- **Error**: `GetMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `MonitorResponse` | `firecrawl/models/monitor_response.py` |
| `GetMonitorErrorBody` | `firecrawl/errors/get_monitor_error.py` |

### client.monitoring.get_monitor_check

- **Route**: `GET /monitor/{monitorId}/checks/{checkId}`
- **Signature**: `def get_monitor_check(monitor_id: UUID, check_id: UUID, *, limit: int | None = 25, skip: int | None = 0, status: Status3OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`, `check_id`
- **Params**: `monitor_id` — path `monitorId` · `check_id` — path `checkId` · `limit` — query · `skip` — query · `status` — query
- **Returns (parsed)**: `MonitorCheckDetailResponse`
- **Returns (raw)**: `ApiResult[MonitorCheckDetailResponse, GetMonitorCheckErrorBody]`
- **Error**: `GetMonitorCheckErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `Status3OrStr` | `firecrawl/models/enums/status3.py` |
| `MonitorCheckDetailResponse` | `firecrawl/models/monitor_check_detail_response.py` |
| `GetMonitorCheckErrorBody` | `firecrawl/errors/get_monitor_check_error.py` |

### client.monitoring.list_monitor_checks

- **Route**: `GET /monitor/{monitorId}/checks`
- **Signature**: `def list_monitor_checks(monitor_id: UUID, *, limit: int | None = 25, offset: int | None = 0, status: Status2OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path `monitorId` · `limit` — query · `offset` — query · `status` — query
- **Returns (parsed)**: `MonitorCheckListResponse`
- **Returns (raw)**: `ApiResult[MonitorCheckListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Status2OrStr` | `firecrawl/models/enums/status2.py` |
| `MonitorCheckListResponse` | `firecrawl/models/monitor_check_list_response.py` |

### client.monitoring.list_monitors

- **Route**: `GET /monitor`
- **Signature**: `def list_monitors(*, limit: int | None = 25, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `offset` — query
- **Returns (parsed)**: `MonitorListResponse`
- **Returns (raw)**: `ApiResult[MonitorListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MonitorListResponse` | `firecrawl/models/monitor_list_response.py` |

### client.monitoring.run_monitor

- **Route**: `POST /monitor/{monitorId}/run`
- **Signature**: `def run_monitor(monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`
- **Params**: `monitor_id` — path `monitorId`
- **Returns (parsed)**: `MonitorRunResponse`
- **Returns (raw)**: `ApiResult[MonitorRunResponse, RunMonitorErrorBody]`
- **Error**: `RunMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [409, anything unmapped]

| Type | Source |
| --- | --- |
| `MonitorRunResponse` | `firecrawl/models/monitor_run_response.py` |
| `RunMonitorErrorBody` | `firecrawl/errors/run_monitor_error.py` |

### client.monitoring.update_monitor

- **Route**: `PATCH /monitor/{monitorId}`
- **Signature**: `def update_monitor(monitor_id: UUID, body: MonitorUpdateRequest | MonitorUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `monitor_id`, `body`
- **Params**: `monitor_id` — path `monitorId` · `body` — JSON body
- **Returns (parsed)**: `MonitorResponse`
- **Returns (raw)**: `ApiResult[MonitorResponse, UpdateMonitorErrorBody]`
- **Error**: `UpdateMonitorErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [404, anything unmapped]

| Type | Source |
| --- | --- |
| `MonitorUpdateRequest` | `firecrawl/models/monitor_update_request.py` |
| `MonitorUpdateRequestDict` | `firecrawl/models/monitor_update_request.py` |
| `MonitorResponse` | `firecrawl/models/monitor_response.py` |
| `UpdateMonitorErrorBody` | `firecrawl/errors/update_monitor_error.py` |

