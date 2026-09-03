# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [FirecrawlApiClient](firecrawl_api/client.py)

## Account

> Source: [Account](firecrawl_api/apis/account.py)

<details>
<summary><code>def get_activity(*, endpoint: Endpoint1OrStr | None = None, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TeamActivityResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists your team's recent API activity from the last 24 hours. Returns metadata about each job including the job ID, which can be used with the corresponding GET endpoint (e.g. GET /crawl/{id}) to retrieve full results. Supports cursor-based pagination and filtering by endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.account.get_activity()
    # TODO: Handle 'response' of type TeamActivityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.account.get_activity()
    # TODO: Handle 'response' of type TeamActivityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>endpoint</code> | <code>[Endpoint1OrStr](firecrawl_api/models/enums/endpoint1.py) \| None</code> | Filter by endpoint<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results per page<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Cursor for pagination. Use the cursor value from the previous response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamActivityResponse](firecrawl_api/models/team_activity_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Agent

> Source: [Agent](firecrawl_api/apis/agent.py)

<details>
<summary><code>def cancel_agent(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> SuccessResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.agent.cancel_agent(job_id)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.agent.cancel_agent(job_id)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | The ID of the agent job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SuccessResponse](firecrawl_api/models/success_response.py)</code> -- Agent job cancelled successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_agent_status(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> AgentResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.agent.get_agent_status(job_id)
    # TODO: Handle 'response' of type AgentResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.agent.get_agent_status(job_id)
    # TODO: Handle 'response' of type AgentResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | The ID of the agent job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AgentResponse1](firecrawl_api/models/agent_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_agent(body: AgentRequest | AgentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AgentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.agent.start_agent(body)
    # TODO: Handle 'response' of type AgentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartAgentErrorBody
```

**Async**

```python
try:
    response = await async_client.agent.start_agent(body)
    # TODO: Handle 'response' of type AgentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartAgentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AgentRequest](firecrawl_api/models/agent_request.py) \| [AgentRequestDict](firecrawl_api/models/agent_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AgentResponse](firecrawl_api/models/agent_response.py)</code> -- Agent task started successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[StartAgentErrorBody](firecrawl_api/errors/start_agent_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Agent402Error1](firecrawl_api/models/agent402_error1.py)</code> |
| 429 | <code>[Agent429Error1](firecrawl_api/models/agent429_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Billing

> Source: [Billing](firecrawl_api/apis/billing.py)

<details>
<summary><code>def get_credit_usage(*, request_options: RequestOptionsOrDict | None = None) -> TeamCreditUsageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing.get_credit_usage()
    # TODO: Handle 'response' of type TeamCreditUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCreditUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.get_credit_usage()
    # TODO: Handle 'response' of type TeamCreditUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCreditUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamCreditUsageResponse](firecrawl_api/models/team_credit_usage_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetCreditUsageErrorBody](firecrawl_api/errors/get_credit_usage_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[TeamCreditUsage404Error1](firecrawl_api/models/team_credit_usage404_error1.py)</code> |
| 500 | <code>[TeamCreditUsage500Error1](firecrawl_api/models/team_credit_usage500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_historical_credit_usage(*, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> TeamCreditUsageHistoricalResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing.get_historical_credit_usage()
    # TODO: Handle 'response' of type TeamCreditUsageHistoricalResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetHistoricalCreditUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.get_historical_credit_usage()
    # TODO: Handle 'response' of type TeamCreditUsageHistoricalResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetHistoricalCreditUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>by_api_key</code> | <code>bool \| None</code> | Get historical credit usage by API key<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamCreditUsageHistoricalResponse](firecrawl_api/models/team_credit_usage_historical_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetHistoricalCreditUsageErrorBody](firecrawl_api/errors/get_historical_credit_usage_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 500 | <code>[TeamCreditUsageHistorical500Error1](firecrawl_api/models/team_credit_usage_historical500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_historical_token_usage(*, by_api_key: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> TeamTokenUsageHistoricalResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing.get_historical_token_usage()
    # TODO: Handle 'response' of type TeamTokenUsageHistoricalResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetHistoricalTokenUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.get_historical_token_usage()
    # TODO: Handle 'response' of type TeamTokenUsageHistoricalResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetHistoricalTokenUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>by_api_key</code> | <code>bool \| None</code> | Get historical token usage by API key<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamTokenUsageHistoricalResponse](firecrawl_api/models/team_token_usage_historical_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetHistoricalTokenUsageErrorBody](firecrawl_api/errors/get_historical_token_usage_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 500 | <code>[TeamTokenUsageHistorical500Error1](firecrawl_api/models/team_token_usage_historical500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_token_usage(*, request_options: RequestOptionsOrDict | None = None) -> TeamTokenUsageResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.billing.get_token_usage()
    # TODO: Handle 'response' of type TeamTokenUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTokenUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.get_token_usage()
    # TODO: Handle 'response' of type TeamTokenUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTokenUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamTokenUsageResponse](firecrawl_api/models/team_token_usage_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetTokenUsageErrorBody](firecrawl_api/errors/get_token_usage_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[TeamTokenUsage404Error1](firecrawl_api/models/team_token_usage404_error1.py)</code> |
| 500 | <code>[TeamTokenUsage500Error1](firecrawl_api/models/team_token_usage500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Crawling

> Source: [Crawling](firecrawl_api/apis/crawling.py)

<details>
<summary><code>def cancel_crawl(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> CrawlResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crawling.cancel_crawl(id)
    # TODO: Handle 'response' of type CrawlResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelCrawlErrorBody
```

**Async**

```python
try:
    response = await async_client.crawling.cancel_crawl(id)
    # TODO: Handle 'response' of type CrawlResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelCrawlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the crawl job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlResponse1](firecrawl_api/models/crawl_response1.py)</code> -- Successful cancellation

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[CancelCrawlErrorBody](firecrawl_api/errors/cancel_crawl_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[Crawl404Error1](firecrawl_api/models/crawl404_error1.py)</code> |
| 500 | <code>[Crawl500Error1](firecrawl_api/models/crawl500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crawl_params_preview(body: CrawlParamsPreviewRequest | CrawlParamsPreviewRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CrawlParamsPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crawling.crawl_params_preview(body)
    # TODO: Handle 'response' of type CrawlParamsPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CrawlParamsPreviewErrorBody
```

**Async**

```python
try:
    response = await async_client.crawling.crawl_params_preview(body)
    # TODO: Handle 'response' of type CrawlParamsPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CrawlParamsPreviewErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CrawlParamsPreviewRequest](firecrawl_api/models/crawl_params_preview_request.py) \| [CrawlParamsPreviewRequestDict](firecrawl_api/models/crawl_params_preview_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlParamsPreviewResponse](firecrawl_api/models/crawl_params_preview_response.py)</code> -- Successful response with generated crawl parameters

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[CrawlParamsPreviewErrorBody](firecrawl_api/errors/crawl_params_preview_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[CrawlParamsPreview400Error1](firecrawl_api/models/crawl_params_preview400_error1.py)</code> |
| 401 | <code>[CrawlParamsPreview401Error1](firecrawl_api/models/crawl_params_preview401_error1.py)</code> |
| 500 | <code>[CrawlParamsPreview500Error1](firecrawl_api/models/crawl_params_preview500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crawl_urls(body: CrawlRequest | CrawlRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CrawlResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crawling.crawl_urls(body)
    # TODO: Handle 'response' of type CrawlResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CrawlUrlsErrorBody
```

**Async**

```python
try:
    response = await async_client.crawling.crawl_urls(body)
    # TODO: Handle 'response' of type CrawlResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CrawlUrlsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CrawlRequest](firecrawl_api/models/crawl_request.py) \| [CrawlRequestDict](firecrawl_api/models/crawl_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlResponse](firecrawl_api/models/crawl_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[CrawlUrlsErrorBody](firecrawl_api/errors/crawl_urls_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Crawl402Error1](firecrawl_api/models/crawl402_error1.py)</code> |
| 429 | <code>[Crawl429Error1](firecrawl_api/models/crawl429_error1.py)</code> |
| 500 | <code>[Crawl500Error1](firecrawl_api/models/crawl500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_active_crawls(*, request_options: RequestOptionsOrDict | None = None) -> CrawlActiveResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crawling.get_active_crawls()
    # TODO: Handle 'response' of type CrawlActiveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetActiveCrawlsErrorBody
```

**Async**

```python
try:
    response = await async_client.crawling.get_active_crawls()
    # TODO: Handle 'response' of type CrawlActiveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetActiveCrawlsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlActiveResponse](firecrawl_api/models/crawl_active_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetActiveCrawlsErrorBody](firecrawl_api/errors/get_active_crawls_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[CrawlActive402Error1](firecrawl_api/models/crawl_active402_error1.py)</code> |
| 429 | <code>[CrawlActive429Error1](firecrawl_api/models/crawl_active429_error1.py)</code> |
| 500 | <code>[CrawlActive500Error1](firecrawl_api/models/crawl_active500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_crawl_errors(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> CrawlErrorsResponseObj</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crawling.get_crawl_errors(id)
    # TODO: Handle 'response' of type CrawlErrorsResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrawlErrorsErrorBody
```

**Async**

```python
try:
    response = await async_client.crawling.get_crawl_errors(id)
    # TODO: Handle 'response' of type CrawlErrorsResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrawlErrorsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the crawl job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlErrorsResponseObj](firecrawl_api/models/crawl_errors_response_obj.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetCrawlErrorsErrorBody](firecrawl_api/errors/get_crawl_errors_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[CrawlErrors402Error1](firecrawl_api/models/crawl_errors402_error1.py)</code> |
| 429 | <code>[CrawlErrors429Error1](firecrawl_api/models/crawl_errors429_error1.py)</code> |
| 500 | <code>[CrawlErrors500Error1](firecrawl_api/models/crawl_errors500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_crawl_status(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> CrawlStatusResponseObj</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.crawling.get_crawl_status(id)
    # TODO: Handle 'response' of type CrawlStatusResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrawlStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.crawling.get_crawl_status(id)
    # TODO: Handle 'response' of type CrawlStatusResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCrawlStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the crawl job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlStatusResponseObj](firecrawl_api/models/crawl_status_response_obj.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetCrawlStatusErrorBody](firecrawl_api/errors/get_crawl_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Crawl402Error1](firecrawl_api/models/crawl402_error1.py)</code> |
| 429 | <code>[Crawl429Error1](firecrawl_api/models/crawl429_error1.py)</code> |
| 500 | <code>[Crawl500Error1](firecrawl_api/models/crawl500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Developer

> Source: [Developer](firecrawl_api/apis/developer.py)

<details>
<summary><code>def developer_search(query: str, *, k: int | None = 10, types: list[Types1OrStr] | None = None, repos: list[str] | None = None, sources: list[str] | None = None, skills: SkillsOrStr | None = None, passages: int | None = 1, language: str | None = None, topic: str | None = None, license: str | None = None, min_stars: int | None = None, max_stars: int | None = None, archived: bool | None = None, fork: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> DeveloperSearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.developer.developer_search(query)
    # TODO: Handle 'response' of type DeveloperSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeveloperSearchErrorBody
```

**Async**

```python
try:
    response = await async_client.developer.developer_search(query)
    # TODO: Handle 'response' of type DeveloperSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeveloperSearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str</code> | Natural-language question or search phrase. |
| <code>k</code> | <code>int \| None</code> | Number of ranked results to return.<br>**Default**: <code>10</code> |
| <code>types</code> | <code>list&#91;[Types1OrStr](firecrawl_api/models/enums/types1.py)&#93; \| None</code> | Result kinds to search. Defaults to all four. Accepts a repeated parameter (`types=issue&types=pull_request`) or one comma-separated value (`types=issue,pull_request`).<br>**Default**: <code>None</code> |
| <code>repos</code> | <code>list&#91;str&#93; \| None</code> | Repository slugs to scope the repository half of the index to, such as `firecrawl/firecrawl`. Applies to the `issue`, `pull_request`, and `readme` types only. Sent together with `sources`, the two halves are combined rather than intersected, so matching results come back from either. Returns 400 when no repository type is in `types`, reporting that `repos` cannot match any requested type and that you should add repository types or drop `repos`.<br>**Default**: <code>None</code> |
| <code>sources</code> | <code>list&#91;str&#93; \| None</code> | Documentation source ids to scope the documentation half to, at most 20. Applies to the `doc` type only. Not a fixed enum: ids reflect the documentation sites in the index and the set grows over time, so confirm an id resolves by sending it and reading the `sources` array on the response. Returns 400 with `sources cannot match any requested type; add doc or drop sources` when `doc` is not in `types`.<br>**Default**: <code>None</code> |
| <code>skills</code> | <code>[SkillsOrStr](firecrawl_api/models/enums/skills.py) \| None</code> | Set to `only` to limit the search to indexed agent-skill files.<br>**Default**: <code>None</code> |
| <code>passages</code> | <code>int \| None</code> | Matched passages to return per result.<br>**Default**: <code>1</code> |
| <code>language</code> | <code>str \| None</code> | Repository primary language, such as `Rust`. Applies to repository results only; sending it with no `sources` scope returns no `doc` results. See [how the repository filters scope a search](/api-reference/endpoint/developer-search#how-the-repository-filters-scope-a-search).<br>**Default**: <code>None</code> |
| <code>topic</code> | <code>str \| None</code> | Repository topic, such as `async`. Applies to repository results only; sending it with no `sources` scope returns no `doc` results.<br>**Default**: <code>None</code> |
| <code>license</code> | <code>str \| None</code> | Repository license, such as `MIT`. Applies to repository results only; sending it with no `sources` scope returns no `doc` results.<br>**Default**: <code>None</code> |
| <code>min_stars</code> | <code>int \| None</code> | Lower bound on repository stars. Applies to repository results only; sending it with no `sources` scope returns no `doc` results.<br>**Default**: <code>None</code> |
| <code>max_stars</code> | <code>int \| None</code> | Upper bound on repository stars. Applies to repository results only; sending it with no `sources` scope returns no `doc` results.<br>**Default**: <code>None</code> |
| <code>archived</code> | <code>bool \| None</code> | Include or exclude archived repositories. Applies to repository results only; sending it with no `sources` scope returns no `doc` results.<br>**Default**: <code>None</code> |
| <code>fork</code> | <code>bool \| None</code> | Include or exclude forks. Applies to repository results only; sending it with no `sources` scope returns no `doc` results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DeveloperSearchResponse](firecrawl_api/models/developer_search_response.py)</code> -- Ranked developer results with matched passages.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[DeveloperSearchErrorBody](firecrawl_api/errors/developer_search_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429, 500 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def developer_search_post(body: SearchDeveloperRequest | SearchDeveloperRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeveloperSearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.developer.developer_search_post(body)
    # TODO: Handle 'response' of type DeveloperSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeveloperSearchPostErrorBody
```

**Async**

```python
try:
    response = await async_client.developer.developer_search_post(body)
    # TODO: Handle 'response' of type DeveloperSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeveloperSearchPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchDeveloperRequest](firecrawl_api/models/search_developer_request.py) \| [SearchDeveloperRequestDict](firecrawl_api/models/search_developer_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DeveloperSearchResponse](firecrawl_api/models/developer_search_response.py)</code> -- Ranked developer results with matched passages.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[DeveloperSearchPostErrorBody](firecrawl_api/errors/developer_search_post_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429, 500 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Extraction

> Source: [Extraction](firecrawl_api/apis/extraction.py)

<details>
<summary><code>def extract_data(body: ExtractRequest | ExtractRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ExtractResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.extraction.extract_data(body)
    # TODO: Handle 'response' of type ExtractResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtractDataErrorBody
```

**Async**

```python
try:
    response = await async_client.extraction.extract_data(body)
    # TODO: Handle 'response' of type ExtractResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExtractDataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ExtractRequest](firecrawl_api/models/extract_request.py) \| [ExtractRequestDict](firecrawl_api/models/extract_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ExtractResponse](firecrawl_api/models/extract_response.py)</code> -- Successful extraction

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ExtractDataErrorBody](firecrawl_api/errors/extract_data_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Extract400Error1](firecrawl_api/models/extract400_error1.py)</code> |
| 500 | <code>[Extract500Error1](firecrawl_api/models/extract500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_extract_status(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ExtractStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.extraction.get_extract_status(id)
    # TODO: Handle 'response' of type ExtractStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.extraction.get_extract_status(id)
    # TODO: Handle 'response' of type ExtractStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the extract job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ExtractStatusResponse](firecrawl_api/models/extract_status_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Feedback

> Source: [Feedback](firecrawl_api/apis/feedback.py)

<details>
<summary><code>def submit_endpoint_feedback(body: EndpointFeedbackRequest | EndpointFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FeedbackResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feedback.submit_endpoint_feedback(body)
    # TODO: Handle 'response' of type FeedbackResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitEndpointFeedbackErrorBody
```

**Async**

```python
try:
    response = await async_client.feedback.submit_endpoint_feedback(body)
    # TODO: Handle 'response' of type FeedbackResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitEndpointFeedbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[EndpointFeedbackRequest](firecrawl_api/models/endpoint_feedback_request.py) \| [EndpointFeedbackRequestDict](firecrawl_api/models/endpoint_feedback_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeedbackResponse](firecrawl_api/models/feedback_response.py)</code> -- Feedback recorded

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[SubmitEndpointFeedbackErrorBody](firecrawl_api/errors/submit_endpoint_feedback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 409, 500 | <code>[FeedbackErrorResponse](firecrawl_api/models/feedback_error_response.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def submit_search_feedback(job_id: UUID, body: SearchFeedbackRequest | SearchFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FeedbackResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feedback.submit_search_feedback(job_id, body)
    # TODO: Handle 'response' of type FeedbackResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitSearchFeedbackErrorBody
```

**Async**

```python
try:
    response = await async_client.feedback.submit_search_feedback(job_id, body)
    # TODO: Handle 'response' of type FeedbackResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitSearchFeedbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | Search job id returned by /search. |
| <code>body</code> | <code>[SearchFeedbackRequest](firecrawl_api/models/search_feedback_request.py) \| [SearchFeedbackRequestDict](firecrawl_api/models/search_feedback_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeedbackResponse](firecrawl_api/models/feedback_response.py)</code> -- Feedback recorded

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[SubmitSearchFeedbackErrorBody](firecrawl_api/errors/submit_search_feedback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 409, 500 | <code>[FeedbackErrorResponse](firecrawl_api/models/feedback_error_response.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Interact

> Source: [Interact](firecrawl_api/apis/interact.py)

<details>
<summary><code>def create_browser_session(body: InteractRequest | InteractRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InteractResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.interact.create_browser_session(body)
    # TODO: Handle 'response' of type InteractResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateBrowserSessionErrorBody
```

**Async**

```python
try:
    response = await async_client.interact.create_browser_session(body)
    # TODO: Handle 'response' of type InteractResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateBrowserSessionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[InteractRequest](firecrawl_api/models/interact_request.py) \| [InteractRequestDict](firecrawl_api/models/interact_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InteractResponse](firecrawl_api/models/interact_response.py)</code> -- Interact session created successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[CreateBrowserSessionErrorBody](firecrawl_api/errors/create_browser_session_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Interact402Error1](firecrawl_api/models/interact402_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_browser_session(session_id: str, *, request_options: RequestOptionsOrDict | None = None) -> InteractResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.interact.delete_browser_session(session_id)
    # TODO: Handle 'response' of type InteractResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteBrowserSessionErrorBody
```

**Async**

```python
try:
    response = await async_client.interact.delete_browser_session(session_id)
    # TODO: Handle 'response' of type InteractResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteBrowserSessionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>session_id</code> | <code>str</code> | The interact session ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InteractResponse2](firecrawl_api/models/interact_response2.py)</code> -- Interact session deleted successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[DeleteBrowserSessionErrorBody](firecrawl_api/errors/delete_browser_session_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Interact402Error1](firecrawl_api/models/interact402_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def execute_browser_code(session_id: str, body: InteractExecuteRequest | InteractExecuteRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> InteractExecuteResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.interact.execute_browser_code(session_id, body)
    # TODO: Handle 'response' of type InteractExecuteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExecuteBrowserCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.interact.execute_browser_code(session_id, body)
    # TODO: Handle 'response' of type InteractExecuteResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExecuteBrowserCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>session_id</code> | <code>str</code> | The interact session ID |
| <code>body</code> | <code>[InteractExecuteRequest](firecrawl_api/models/interact_execute_request.py) \| [InteractExecuteRequestDict](firecrawl_api/models/interact_execute_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InteractExecuteResponse](firecrawl_api/models/interact_execute_response.py)</code> -- Code executed successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ExecuteBrowserCodeErrorBody](firecrawl_api/errors/execute_browser_code_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[InteractExecute402Error1](firecrawl_api/models/interact_execute402_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_browser_sessions(*, status: Status10OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> InteractResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.interact.list_browser_sessions()
    # TODO: Handle 'response' of type InteractResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListBrowserSessionsErrorBody
```

**Async**

```python
try:
    response = await async_client.interact.list_browser_sessions()
    # TODO: Handle 'response' of type InteractResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListBrowserSessionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>status</code> | <code>[Status10OrStr](firecrawl_api/models/enums/status10.py) \| None</code> | Filter sessions by status<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InteractResponse1](firecrawl_api/models/interact_response1.py)</code> -- List of interact sessions

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ListBrowserSessionsErrorBody](firecrawl_api/errors/list_browser_sessions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Interact402Error1](firecrawl_api/models/interact402_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## MappingApi

> Source: [MappingApi](firecrawl_api/apis/mapping_api.py)

<details>
<summary><code>def map_urls(body: MapRequest | MapRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> MapResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.mapping_api.map_urls(body)
    # TODO: Handle 'response' of type MapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MapUrlsErrorBody
```

**Async**

```python
try:
    response = await async_client.mapping_api.map_urls(body)
    # TODO: Handle 'response' of type MapResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MapUrlsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[MapRequest](firecrawl_api/models/map_request.py) \| [MapRequestDict](firecrawl_api/models/map_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MapResponse](firecrawl_api/models/map_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[MapUrlsErrorBody](firecrawl_api/errors/map_urls_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Map402Error1](firecrawl_api/models/map402_error1.py)</code> |
| 429 | <code>[Map429Error1](firecrawl_api/models/map429_error1.py)</code> |
| 500 | <code>[Map500Error1](firecrawl_api/models/map500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Miscellaneous

> Source: [Miscellaneous](firecrawl_api/apis/miscellaneous.py)

<details>
<summary><code>def get_queue_status(*, request_options: RequestOptionsOrDict | None = None) -> TeamQueueStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.miscellaneous.get_queue_status()
    # TODO: Handle 'response' of type TeamQueueStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.miscellaneous.get_queue_status()
    # TODO: Handle 'response' of type TeamQueueStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamQueueStatusResponse](firecrawl_api/models/team_queue_status_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Monitoring

> Source: [Monitoring](firecrawl_api/apis/monitoring.py)

<details>
<summary><code>def create_monitor(body: MonitorCreateRequest | MonitorCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> MonitorResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.create_monitor(body)
    # TODO: Handle 'response' of type MonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitoring.create_monitor(body)
    # TODO: Handle 'response' of type MonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[MonitorCreateRequest](firecrawl_api/models/monitor_create_request.py) \| [MonitorCreateRequestDict](firecrawl_api/models/monitor_create_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorResponse](firecrawl_api/models/monitor_response.py)</code> -- Monitor created

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[CreateMonitorErrorBody](firecrawl_api/errors/create_monitor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_monitor(monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> SuccessResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.delete_monitor(monitor_id)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitoring.delete_monitor(monitor_id)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>UUID</code> | The monitor ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SuccessResponse](firecrawl_api/models/success_response.py)</code> -- Monitor deleted

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[DeleteMonitorErrorBody](firecrawl_api/errors/delete_monitor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_monitor(monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> MonitorResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.get_monitor(monitor_id)
    # TODO: Handle 'response' of type MonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitoring.get_monitor(monitor_id)
    # TODO: Handle 'response' of type MonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>UUID</code> | The monitor ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorResponse](firecrawl_api/models/monitor_response.py)</code> -- Monitor details

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetMonitorErrorBody](firecrawl_api/errors/get_monitor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_monitor_check(monitor_id: UUID, check_id: UUID, *, limit: int | None = 25, skip: int | None = 0, status: Status3OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> MonitorCheckDetailResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.get_monitor_check(monitor_id, check_id)
    # TODO: Handle 'response' of type MonitorCheckDetailResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMonitorCheckErrorBody
```

**Async**

```python
try:
    response = await async_client.monitoring.get_monitor_check(monitor_id, check_id)
    # TODO: Handle 'response' of type MonitorCheckDetailResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMonitorCheckErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>UUID</code> | The monitor ID |
| <code>check_id</code> | <code>UUID</code> | The monitor check ID |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>25</code> |
| <code>skip</code> | <code>int \| None</code> | Number of page results to skip. Use the `next` URL from the previous response for pagination.<br>**Default**: <code>0</code> |
| <code>status</code> | <code>[Status3OrStr](firecrawl_api/models/enums/status3.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorCheckDetailResponse](firecrawl_api/models/monitor_check_detail_response.py)</code> -- Monitor check details

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetMonitorCheckErrorBody](firecrawl_api/errors/get_monitor_check_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_monitor_checks(monitor_id: UUID, *, limit: int | None = 25, offset: int | None = 0, status: Status2OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> MonitorCheckListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.list_monitor_checks(monitor_id)
    # TODO: Handle 'response' of type MonitorCheckListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.monitoring.list_monitor_checks(monitor_id)
    # TODO: Handle 'response' of type MonitorCheckListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>UUID</code> | The monitor ID |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>25</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>status</code> | <code>[Status2OrStr](firecrawl_api/models/enums/status2.py) \| None</code> | Filter checks by status.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorCheckListResponse](firecrawl_api/models/monitor_check_list_response.py)</code> -- Monitor checks

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_monitors(*, limit: int | None = 25, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> MonitorListResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.list_monitors()
    # TODO: Handle 'response' of type MonitorListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.monitoring.list_monitors()
    # TODO: Handle 'response' of type MonitorListResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>25</code> |
| <code>offset</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorListResponse](firecrawl_api/models/monitor_list_response.py)</code> -- List of monitors

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RawError](firecrawl_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def run_monitor(monitor_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> MonitorRunResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.run_monitor(monitor_id)
    # TODO: Handle 'response' of type MonitorRunResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RunMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitoring.run_monitor(monitor_id)
    # TODO: Handle 'response' of type MonitorRunResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RunMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>UUID</code> | The monitor ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorRunResponse](firecrawl_api/models/monitor_run_response.py)</code> -- Monitor check queued

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[RunMonitorErrorBody](firecrawl_api/errors/run_monitor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 409 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_monitor(monitor_id: UUID, body: MonitorUpdateRequest | MonitorUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> MonitorResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.monitoring.update_monitor(monitor_id, body)
    # TODO: Handle 'response' of type MonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMonitorErrorBody
```

**Async**

```python
try:
    response = await async_client.monitoring.update_monitor(monitor_id, body)
    # TODO: Handle 'response' of type MonitorResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateMonitorErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>monitor_id</code> | <code>UUID</code> | The monitor ID |
| <code>body</code> | <code>[MonitorUpdateRequest](firecrawl_api/models/monitor_update_request.py) \| [MonitorUpdateRequestDict](firecrawl_api/models/monitor_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MonitorResponse](firecrawl_api/models/monitor_response.py)</code> -- Monitor updated

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[UpdateMonitorErrorBody](firecrawl_api/errors/update_monitor_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ResearchApi

> Source: [ResearchApi](firecrawl_api/apis/research_api.py)

<details>
<summary><code>def research_get_paper(id: str, *, query: str | None = None, k: int | None = 4, request_options: RequestOptionsOrDict | None = None) -> SearchResearchPapersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.research_api.research_get_paper(id)
    # TODO: Handle 'response' of type SearchResearchPapersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchGetPaperErrorBody
```

**Async**

```python
try:
    response = await async_client.research_api.research_get_paper(id)
    # TODO: Handle 'response' of type SearchResearchPapersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchGetPaperErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Paper reference: a canonical paperId or source-specific primaryId. |
| <code>query</code> | <code>str \| None</code> | When present, returns the top matching full-text passages for this question. Omit it to inspect metadata only.<br>**Default**: <code>None</code> |
| <code>k</code> | <code>int \| None</code> | Passage count for read mode. Only valid when query is present.<br>**Default**: <code>4</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SearchResearchPapersResponse](firecrawl_api/models/unions/search_research_papers_response.py)</code> -- Paper metadata or read-mode passages.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ResearchGetPaperErrorBody](firecrawl_api/errors/research_get_paper_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 429, 500 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def research_related_papers(id: str, intent: str, *, mode: Mode5OrStr | None = None, k: int | None = 40, rerank: bool | None = None, anchor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ResearchSimilarPapersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.research_api.research_related_papers(id, intent)
    # TODO: Handle 'response' of type ResearchSimilarPapersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchRelatedPapersErrorBody
```

**Async**

```python
try:
    response = await async_client.research_api.research_related_papers(id, intent)
    # TODO: Handle 'response' of type ResearchSimilarPapersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchRelatedPapersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Primary seed paper reference. |
| <code>intent</code> | <code>str</code> | Natural-language ranking/filtering intent used for semantic ranking. |
| <code>mode</code> | <code>[Mode5OrStr](firecrawl_api/models/enums/mode5.py) \| None</code> | Structural expansion mode.<br>**Default**: <code>None</code> |
| <code>k</code> | <code>int \| None</code> | Maximum number of related papers to return.<br>**Default**: <code>40</code> |
| <code>rerank</code> | <code>bool \| None</code> | Apply an additional rerank over fused candidates.<br>**Default**: <code>None</code> |
| <code>anchor</code> | <code>str \| None</code> | Additional seed paper reference. Repeat this parameter for multiple anchors.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ResearchSimilarPapersResponse](firecrawl_api/models/research_similar_papers_response.py)</code> -- Ranked related papers.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ResearchRelatedPapersErrorBody](firecrawl_api/errors/research_related_papers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429, 500 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def research_search_papers(query: str, *, k: int | None = 40, authors: str | None = None, categories: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ResearchSearchPapersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.research_api.research_search_papers(query)
    # TODO: Handle 'response' of type ResearchSearchPapersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchSearchPapersErrorBody
```

**Async**

```python
try:
    response = await async_client.research_api.research_search_papers(query)
    # TODO: Handle 'response' of type ResearchSearchPapersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResearchSearchPapersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str</code> | Natural-language paper search query. |
| <code>k</code> | <code>int \| None</code> | Maximum number of ranked papers to return.<br>**Default**: <code>40</code> |
| <code>authors</code> | <code>str \| None</code> | Author substring filter. Repeat or pass a comma-separated value; all filters must match.<br>**Default**: <code>None</code> |
| <code>categories</code> | <code>str \| None</code> | Paper category filter. Repeat or pass a comma-separated value; all filters must match.<br>**Default**: <code>None</code> |
| <code>from_</code> | <code>Date \| None</code> | Inclusive lower bound on created/updated date.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | Inclusive upper bound on created/updated date.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ResearchSearchPapersResponse](firecrawl_api/models/research_search_papers_response.py)</code> -- Ranked paper results.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ResearchSearchPapersErrorBody](firecrawl_api/errors/research_search_papers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429, 500 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Scraping

> Source: [Scraping](firecrawl_api/apis/scraping.py)

<details>
<summary><code>def cancel_batch_scrape(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> BatchScrapeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.cancel_batch_scrape(id)
    # TODO: Handle 'response' of type BatchScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelBatchScrapeErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.cancel_batch_scrape(id)
    # TODO: Handle 'response' of type BatchScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelBatchScrapeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the batch scrape job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchScrapeResponse](firecrawl_api/models/batch_scrape_response.py)</code> -- Successful cancellation

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[CancelBatchScrapeErrorBody](firecrawl_api/errors/cancel_batch_scrape_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 404 | <code>[BatchScrape404Error1](firecrawl_api/models/batch_scrape404_error1.py)</code> |
| 500 | <code>[BatchScrape500Error1](firecrawl_api/models/batch_scrape500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_batch_scrape_errors(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> CrawlErrorsResponseObj</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.get_batch_scrape_errors(id)
    # TODO: Handle 'response' of type CrawlErrorsResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBatchScrapeErrorsErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.get_batch_scrape_errors(id)
    # TODO: Handle 'response' of type CrawlErrorsResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBatchScrapeErrorsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the batch scrape job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CrawlErrorsResponseObj](firecrawl_api/models/crawl_errors_response_obj.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetBatchScrapeErrorsErrorBody](firecrawl_api/errors/get_batch_scrape_errors_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[BatchScrapeErrors402Error1](firecrawl_api/models/batch_scrape_errors402_error1.py)</code> |
| 429 | <code>[BatchScrapeErrors429Error1](firecrawl_api/models/batch_scrape_errors429_error1.py)</code> |
| 500 | <code>[BatchScrapeErrors500Error1](firecrawl_api/models/batch_scrape_errors500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_batch_scrape_status(id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> BatchScrapeStatusResponseObj</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.get_batch_scrape_status(id)
    # TODO: Handle 'response' of type BatchScrapeStatusResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBatchScrapeStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.get_batch_scrape_status(id)
    # TODO: Handle 'response' of type BatchScrapeStatusResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBatchScrapeStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>UUID</code> | The ID of the batch scrape job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchScrapeStatusResponseObj](firecrawl_api/models/batch_scrape_status_response_obj.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetBatchScrapeStatusErrorBody](firecrawl_api/errors/get_batch_scrape_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[BatchScrape402Error1](firecrawl_api/models/batch_scrape402_error1.py)</code> |
| 429 | <code>[BatchScrape429Error1](firecrawl_api/models/batch_scrape429_error1.py)</code> |
| 500 | <code>[BatchScrape500Error1](firecrawl_api/models/batch_scrape500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_scrape_status(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ScrapeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.get_scrape_status(job_id)
    # TODO: Handle 'response' of type ScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetScrapeStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.get_scrape_status(job_id)
    # TODO: Handle 'response' of type ScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetScrapeStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | The ID of the job |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScrapeResponse](firecrawl_api/models/scrape_response.py)</code> -- Scrape job status

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetScrapeStatusErrorBody](firecrawl_api/errors/get_scrape_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Scrape402Error21](firecrawl_api/models/scrape402_error21.py)</code> |
| 429 | <code>[Scrape429Error21](firecrawl_api/models/scrape429_error21.py)</code> |
| 500 | <code>[Scrape500Error21](firecrawl_api/models/scrape500_error21.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def interact_with_scrape_browser_session(job_id: UUID, body: ScrapeInteractRequest | ScrapeInteractRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ScrapeInteractResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.interact_with_scrape_browser_session(job_id, body)
    # TODO: Handle 'response' of type ScrapeInteractResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InteractWithScrapeBrowserSessionErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.interact_with_scrape_browser_session(job_id, body)
    # TODO: Handle 'response' of type ScrapeInteractResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InteractWithScrapeBrowserSessionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | The scrape job ID |
| <code>body</code> | <code>[ScrapeInteractRequest](firecrawl_api/models/scrape_interact_request.py) \| [ScrapeInteractRequestDict](firecrawl_api/models/scrape_interact_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScrapeInteractResponse](firecrawl_api/models/scrape_interact_response.py)</code> -- Code executed successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[InteractWithScrapeBrowserSessionErrorBody](firecrawl_api/errors/interact_with_scrape_browser_session_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ScrapeInteract400Error1](firecrawl_api/models/scrape_interact400_error1.py)</code> |
| 402 | <code>[ScrapeInteract402Error1](firecrawl_api/models/scrape_interact402_error1.py)</code> |
| 403 | <code>[ScrapeInteract403Error1](firecrawl_api/models/scrape_interact403_error1.py)</code> |
| 404 | <code>[ScrapeInteract404Error1](firecrawl_api/models/scrape_interact404_error1.py)</code> |
| 409 | <code>[ScrapeInteract409Error1](firecrawl_api/models/scrape_interact409_error1.py)</code> |
| 410 | <code>[ScrapeInteract410Error1](firecrawl_api/models/scrape_interact410_error1.py)</code> |
| 429 | <code>[ScrapeInteract429Error1](firecrawl_api/models/scrape_interact429_error1.py)</code> |
| 502 | <code>[ScrapeInteract502Error1](firecrawl_api/models/scrape_interact502_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def parse_file(file: bytes, *, options: ParseOptions | ParseOptionsDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ScrapeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.parse_file(file)
    # TODO: Handle 'response' of type ScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ParseFileErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.parse_file(file)
    # TODO: Handle 'response' of type ScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ParseFileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file</code> | <code>bytes</code> | The file bytes to parse. Supported extensions: .html, .htm, .xhtml, .pdf, .docx, .doc, .docm, .odt, .ods, .odp, .rtf, .xlsx, .xls, .xlsm, .xlsb, .pptx, .ppt, .pptm, .epub, .csv. |
| <code>options</code> | <code>[ParseOptions](firecrawl_api/models/parse_options.py) \| [ParseOptionsDict](firecrawl_api/models/parse_options.py) \| None</code> | Optional parse options sent as JSON in the multipart `options` field.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScrapeResponse](firecrawl_api/models/scrape_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ParseFileErrorBody](firecrawl_api/errors/parse_file_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[Parse400Error1](firecrawl_api/models/parse400_error1.py)</code> |
| 402 | <code>[Parse402Error1](firecrawl_api/models/parse402_error1.py)</code> |
| 429 | <code>[Parse429Error1](firecrawl_api/models/parse429_error1.py)</code> |
| 500 | <code>[Parse500Error1](firecrawl_api/models/parse500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def scrape_and_extract_from_url(body: ScrapeRequest | ScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ScrapeResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.scrape_and_extract_from_url(body)
    # TODO: Handle 'response' of type ScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScrapeAndExtractFromUrlErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.scrape_and_extract_from_url(body)
    # TODO: Handle 'response' of type ScrapeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScrapeAndExtractFromUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ScrapeRequest](firecrawl_api/models/scrape_request.py) \| [ScrapeRequestDict](firecrawl_api/models/scrape_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScrapeResponse](firecrawl_api/models/scrape_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ScrapeAndExtractFromUrlErrorBody](firecrawl_api/errors/scrape_and_extract_from_url_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[Scrape402Error1](firecrawl_api/models/scrape402_error1.py)</code> |
| 429 | <code>[Scrape429Error1](firecrawl_api/models/scrape429_error1.py)</code> |
| 500 | <code>[Scrape500Error1](firecrawl_api/models/scrape500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def scrape_and_extract_from_urls(body: BatchScrapeRequest | BatchScrapeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BatchScrapeResponseObj</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.scrape_and_extract_from_urls(body)
    # TODO: Handle 'response' of type BatchScrapeResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScrapeAndExtractFromUrlsErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.scrape_and_extract_from_urls(body)
    # TODO: Handle 'response' of type BatchScrapeResponseObj
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScrapeAndExtractFromUrlsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchScrapeRequest](firecrawl_api/models/batch_scrape_request.py) \| [BatchScrapeRequestDict](firecrawl_api/models/batch_scrape_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BatchScrapeResponseObj](firecrawl_api/models/batch_scrape_response_obj.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[ScrapeAndExtractFromUrlsErrorBody](firecrawl_api/errors/scrape_and_extract_from_urls_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 402 | <code>[BatchScrape402Error1](firecrawl_api/models/batch_scrape402_error1.py)</code> |
| 429 | <code>[BatchScrape429Error1](firecrawl_api/models/batch_scrape429_error1.py)</code> |
| 500 | <code>[BatchScrape500Error1](firecrawl_api/models/batch_scrape500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_interactive_scrape_browser_session(job_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> SuccessResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.scraping.stop_interactive_scrape_browser_session(job_id)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StopInteractiveScrapeBrowserSessionErrorBody
```

**Async**

```python
try:
    response = await async_client.scraping.stop_interactive_scrape_browser_session(job_id)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StopInteractiveScrapeBrowserSessionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | The scrape job ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SuccessResponse](firecrawl_api/models/success_response.py)</code> -- Interactive scrape browser session stopped successfully

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[StopInteractiveScrapeBrowserSessionErrorBody](firecrawl_api/errors/stop_interactive_scrape_browser_session_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[ScrapeInteract403Error1](firecrawl_api/models/scrape_interact403_error1.py)</code> |
| 404 | <code>[ScrapeInteract404Error1](firecrawl_api/models/scrape_interact404_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Search

> Source: [Search](firecrawl_api/apis/search.py)

<details>
<summary><code>def search_and_scrape(body: SearchRequest | SearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search.search_and_scrape(body)
    # TODO: Handle 'response' of type SearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchAndScrapeErrorBody
```

**Async**

```python
try:
    response = await async_client.search.search_and_scrape(body)
    # TODO: Handle 'response' of type SearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchAndScrapeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchRequest](firecrawl_api/models/search_request.py) \| [SearchRequestDict](firecrawl_api/models/search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SearchResponse](firecrawl_api/models/search_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[SearchAndScrapeErrorBody](firecrawl_api/errors/search_and_scrape_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 408 | <code>[Search408Error1](firecrawl_api/models/search408_error1.py)</code> |
| 500 | <code>[Search500Error1](firecrawl_api/models/search500_error1.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def submit_search_feedback(job_id: UUID, body: SearchFeedbackRequest | SearchFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FeedbackResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search.submit_search_feedback(job_id, body)
    # TODO: Handle 'response' of type FeedbackResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitSearchFeedbackErrorBody
```

**Async**

```python
try:
    response = await async_client.search.submit_search_feedback(job_id, body)
    # TODO: Handle 'response' of type FeedbackResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitSearchFeedbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>UUID</code> | Search job id returned by /search. |
| <code>body</code> | <code>[SearchFeedbackRequest](firecrawl_api/models/search_feedback_request.py) \| [SearchFeedbackRequestDict](firecrawl_api/models/search_feedback_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FeedbackResponse](firecrawl_api/models/feedback_response.py)</code> -- Feedback recorded

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[SubmitSearchFeedbackErrorBody](firecrawl_api/errors/submit_search_feedback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 409, 500 | <code>[FeedbackErrorResponse](firecrawl_api/models/feedback_error_response.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Support

> Source: [Support](firecrawl_api/apis/support.py)

<details>
<summary><code>def ask_support_agent(body: SupportAskRequest | SupportAskRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SupportAskResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Diagnose Firecrawl job, account, and API usage issues with an AI support agent.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.support.ask_support_agent(body)
    # TODO: Handle 'response' of type SupportAskResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AskSupportAgentErrorBody
```

**Async**

```python
try:
    response = await async_client.support.ask_support_agent(body)
    # TODO: Handle 'response' of type SupportAskResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AskSupportAgentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SupportAskRequest](firecrawl_api/models/support_ask_request.py) \| [SupportAskRequestDict](firecrawl_api/models/support_ask_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SupportAskResponse](firecrawl_api/models/support_ask_response.py)</code> -- Support agent answer

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[AskSupportAgentErrorBody](firecrawl_api/errors/ask_support_agent_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 503, 504 | <code>[SupportProxyErrorResponse](firecrawl_api/models/support_proxy_error_response.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_support_docs(body: SupportDocsSearchRequest | SupportDocsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SupportDocsSearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Answer Firecrawl documentation questions using the public docs corpus.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.support.search_support_docs(body)
    # TODO: Handle 'response' of type SupportDocsSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchSupportDocsErrorBody
```

**Async**

```python
try:
    response = await async_client.support.search_support_docs(body)
    # TODO: Handle 'response' of type SupportDocsSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchSupportDocsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SupportDocsSearchRequest](firecrawl_api/models/support_docs_search_request.py) \| [SupportDocsSearchRequestDict](firecrawl_api/models/support_docs_search_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SupportDocsSearchResponse](firecrawl_api/models/support_docs_search_response.py)</code> -- Docs-grounded answer

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[SearchSupportDocsErrorBody](firecrawl_api/errors/search_support_docs_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 503, 504 | <code>[SupportProxyErrorResponse](firecrawl_api/models/support_proxy_error_response.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ThreatProtection

> Source: [ThreatProtection](firecrawl_api/apis/threat_protection.py)

<details>
<summary><code>def get_threat_protection(*, request_options: RequestOptionsOrDict | None = None) -> TeamThreatProtectionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.threat_protection.get_threat_protection()
    # TODO: Handle 'response' of type TeamThreatProtectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetThreatProtectionErrorBody
```

**Async**

```python
try:
    response = await async_client.threat_protection.get_threat_protection()
    # TODO: Handle 'response' of type TeamThreatProtectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetThreatProtectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamThreatProtectionResponse](firecrawl_api/models/team_threat_protection_response.py)</code> -- Effective threat protection policy for the team's organization.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[GetThreatProtectionErrorBody](firecrawl_api/errors/get_threat_protection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_threat_protection(body: TeamThreatProtectionRequest | TeamThreatProtectionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TeamThreatProtectionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full-document update. Unspecified fields reset to defaults. Enterprise feature, team admins only.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.threat_protection.update_threat_protection(body)
    # TODO: Handle 'response' of type TeamThreatProtectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateThreatProtectionErrorBody
```

**Async**

```python
try:
    response = await async_client.threat_protection.update_threat_protection(body)
    # TODO: Handle 'response' of type TeamThreatProtectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateThreatProtectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TeamThreatProtectionRequest](firecrawl_api/models/team_threat_protection_request.py) \| [TeamThreatProtectionRequestDict](firecrawl_api/models/team_threat_protection_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](firecrawl_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamThreatProtectionResponse](firecrawl_api/models/team_threat_protection_response.py)</code> -- Effective threat protection policy for the team's organization.

**OnError**: <code>[ApiError](firecrawl_api/core/exceptions.py)&#91;[UpdateThreatProtectionErrorBody](firecrawl_api/errors/update_threat_protection_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403 | <code>[RawError](firecrawl_api/core/results.py)</code> |
| anything unmapped | <code>[RawError](firecrawl_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

