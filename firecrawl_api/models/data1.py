from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .actions import Actions, ActionsDict
from .branding1 import Branding1, Branding1Dict
from .change_tracking1 import ChangeTracking1, ChangeTracking1Dict
from .menu1 import Menu1, Menu1Dict
from .metadata import Metadata, MetadataDict
from .product1 import Product1, Product1Dict


class Data1(SdkBaseModel):
    markdown: Optional[str] = UNSET
    summary: OptionalNullable[str] = UNSET
    """Summary of the page if ``summary`` is in ``formats``"""

    html: OptionalNullable[str] = UNSET
    """Cleaned HTML of the page if ``html`` is in ``formats``. Removes ``<script>``, ``<style>``, ``<noscript>``,
    ``<meta>``, and ``<head>`` tags; converts relative URLs to absolute; resolves responsive image ``srcset`` to the
    largest version. Respects ``onlyMainContent``, ``includeTags``, and ``excludeTags`` filters."""

    raw_html: OptionalNullable[str] = Field(default=UNSET, alias="rawHtml")
    """The exact, unmodified HTML as received from the page if ``rawHtml`` is in ``formats``. No cleaning or filtering
    is applied."""

    screenshot: OptionalNullable[str] = UNSET
    """Screenshot of the page if ``screenshot`` is in ``formats``. Screenshots expire after 24 hours and can no longer
    be downloaded."""

    audio: OptionalNullable[str] = UNSET
    """Signed URL to the extracted MP3 audio file if ``audio`` is in ``formats``. The signed URL expires after 1
    hour."""

    video: OptionalNullable[str] = UNSET
    """Signed URL to the extracted video file if ``video`` is in ``formats``. The signed URL expires after 1 hour."""

    answer: OptionalNullable[str] = UNSET
    """Natural-language answer to the question supplied via the ``question`` format. Only present if a ``question``
    format object was included in ``formats``."""

    highlights: OptionalNullable[str] = UNSET
    """Relevant source text selected by the ``highlights`` format. Only present if a ``highlights`` format object was
    included in ``formats``."""

    links: Optional[list[str]] = UNSET
    """List of links on the page if ``links`` is in ``formats``"""

    actions: OptionalNullable[Actions] = UNSET
    """Results of the actions specified in the ``actions`` parameter. Only present if the ``actions`` parameter was
    provided in the request"""

    metadata: Optional[Metadata] = UNSET
    warning: OptionalNullable[str] = UNSET
    """Can be displayed when using LLM Extraction. Warning message will let you know any issues with the extraction."""

    change_tracking: OptionalNullable[ChangeTracking1] = Field(default=UNSET, alias="changeTracking")
    """Change tracking information if ``changeTracking`` is in ``formats``. Only present when the ``changeTracking``
    format is requested."""

    branding: OptionalNullable[Branding1] = UNSET
    """Branding information extracted from the page if ``branding`` is in ``formats``. Includes colors, fonts,
    typography, spacing, components, and more."""

    product: OptionalNullable[Product1] = UNSET
    """Product information extracted from the page if ``product`` is in ``formats``. Includes title, brand, category,
    description, and variants. Pricing, availability, and images live on each variant."""

    menu: OptionalNullable[Menu1] = UNSET
    """Menu information extracted from the page if ``menu`` is in ``formats``. Includes the merchant, currency, and a
    list of sections, where each section carries items with description, images, price, availability, dietary tags,
    calories, and option groups."""


class Data1Dict(TypedDict):
    markdown: NotRequired[str]
    summary: NotRequired[str | None]
    html: NotRequired[str | None]
    raw_html: NotRequired[str | None]
    screenshot: NotRequired[str | None]
    audio: NotRequired[str | None]
    video: NotRequired[str | None]
    answer: NotRequired[str | None]
    highlights: NotRequired[str | None]
    links: NotRequired[list[str]]
    actions: NotRequired[Actions | ActionsDict | None]
    metadata: NotRequired[Metadata | MetadataDict]
    warning: NotRequired[str | None]
    change_tracking: NotRequired[ChangeTracking1 | ChangeTracking1Dict | None]
    branding: NotRequired[Branding1 | Branding1Dict | None]
    product: NotRequired[Product1 | Product1Dict | None]
    menu: NotRequired[Menu1 | Menu1Dict | None]
