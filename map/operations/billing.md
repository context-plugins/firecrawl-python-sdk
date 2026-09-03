<!-- Generated file — do not edit; regenerated with the SDK. -->

# Billing — operations

Accessor: `client.billing` · Source: `firecrawl_api/apis/billing.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.billing.get_credit_usage

- **Route**: `GET /team/credit-usage`
- **Auth**: `bearer_auth`
- **Signature**: `def get_credit_usage(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TeamCreditUsageResponse`
- **Returns (raw)**: `ApiResult[TeamCreditUsageResponse, GetCreditUsageErrorBody]`
- **Error**: `GetCreditUsageErrorBody` — **Case A (typed)**
- **Error arms**: `TeamCreditUsage404Error1` [404] · `TeamCreditUsage500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamCreditUsageResponse` | `firecrawl_api/models/team_credit_usage_response.py` |
| `GetCreditUsageErrorBody` | `firecrawl_api/errors/get_credit_usage_error.py` |
| `TeamCreditUsage404Error1` | `firecrawl_api/models/team_credit_usage404_error1.py` |
| `TeamCreditUsage500Error1` | `firecrawl_api/models/team_credit_usage500_error1.py` |

### client.billing.get_historical_credit_usage

- **Route**: `GET /team/credit-usage/historical`
- **Auth**: `bearer_auth`
- **Signature**: `def get_historical_credit_usage(*, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `by_api_key` — query `byApiKey`
- **Returns (parsed)**: `TeamCreditUsageHistoricalResponse`
- **Returns (raw)**: `ApiResult[TeamCreditUsageHistoricalResponse, GetHistoricalCreditUsageErrorBody]`
- **Error**: `GetHistoricalCreditUsageErrorBody` — **Case A (typed)**
- **Error arms**: `TeamCreditUsageHistorical500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamCreditUsageHistoricalResponse` | `firecrawl_api/models/team_credit_usage_historical_response.py` |
| `GetHistoricalCreditUsageErrorBody` | `firecrawl_api/errors/get_historical_credit_usage_error.py` |
| `TeamCreditUsageHistorical500Error1` | `firecrawl_api/models/team_credit_usage_historical500_error1.py` |

### client.billing.get_historical_token_usage

- **Route**: `GET /team/token-usage/historical`
- **Auth**: `bearer_auth`
- **Signature**: `def get_historical_token_usage(*, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `by_api_key` — query `byApiKey`
- **Returns (parsed)**: `TeamTokenUsageHistoricalResponse`
- **Returns (raw)**: `ApiResult[TeamTokenUsageHistoricalResponse, GetHistoricalTokenUsageErrorBody]`
- **Error**: `GetHistoricalTokenUsageErrorBody` — **Case A (typed)**
- **Error arms**: `TeamTokenUsageHistorical500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamTokenUsageHistoricalResponse` | `firecrawl_api/models/team_token_usage_historical_response.py` |
| `GetHistoricalTokenUsageErrorBody` | `firecrawl_api/errors/get_historical_token_usage_error.py` |
| `TeamTokenUsageHistorical500Error1` | `firecrawl_api/models/team_token_usage_historical500_error1.py` |

### client.billing.get_token_usage

- **Route**: `GET /team/token-usage`
- **Auth**: `bearer_auth`
- **Signature**: `def get_token_usage(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `TeamTokenUsageResponse`
- **Returns (raw)**: `ApiResult[TeamTokenUsageResponse, GetTokenUsageErrorBody]`
- **Error**: `GetTokenUsageErrorBody` — **Case A (typed)**
- **Error arms**: `TeamTokenUsage404Error1` [404] · `TeamTokenUsage500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TeamTokenUsageResponse` | `firecrawl_api/models/team_token_usage_response.py` |
| `GetTokenUsageErrorBody` | `firecrawl_api/errors/get_token_usage_error.py` |
| `TeamTokenUsage404Error1` | `firecrawl_api/models/team_token_usage404_error1.py` |
| `TeamTokenUsage500Error1` | `firecrawl_api/models/team_token_usage500_error1.py` |

