from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Location(SdkBaseModel):
    """Location settings for the request. When specified, this will use an appropriate proxy if available and emulate
    the corresponding language and timezone settings. Defaults to 'US' if not specified."""

    country: Optional[str] = UNSET
    """ISO 3166-1 alpha-2 country code (e.g., 'US', 'AU', 'DE', 'JP')"""

    languages: Optional[list[str]] = UNSET
    """Preferred languages and locales for the request in order of priority. Defaults to the language of the specified
    location. See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language"""


class LocationDict(TypedDict):
    country: NotRequired[str]
    languages: NotRequired[list[str]]
