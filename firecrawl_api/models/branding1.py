from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .colors import Colors, ColorsDict
from .components import Components, ComponentsDict
from .enums.color_scheme import ColorSchemeOrStr
from .font import Font, FontDict
from .images2 import Images2, Images2Dict
from .spacing import Spacing, SpacingDict
from .typography import Typography, TypographyDict


class Branding1(SdkBaseModel):
    """Branding information extracted from the page if ``branding`` is in ``formats``. Includes colors, fonts,
    typography, spacing, components, and more."""

    color_scheme: Optional[ColorSchemeOrStr] = Field(default=UNSET, alias="colorScheme")
    """The detected color scheme of the page."""

    logo: OptionalNullable[str] = UNSET
    """URL of the primary logo."""

    colors: OptionalNullable[Colors] = UNSET
    """Brand colors extracted from the page."""

    fonts: Optional[list[Font | None]] = UNSET
    """Array of font families used on the page."""

    typography: OptionalNullable[Typography] = UNSET
    """Detailed typography information."""

    spacing: OptionalNullable[Spacing] = UNSET
    """Spacing and layout information."""

    components: OptionalNullable[Components] = UNSET
    """UI component styles."""

    icons: OptionalNullable[Any] = UNSET
    """Icon style information."""

    images: OptionalNullable[Images2] = UNSET
    """Brand images."""

    animations: OptionalNullable[Any] = UNSET
    """Animation and transition settings."""

    layout: OptionalNullable[Any] = UNSET
    """Layout configuration (grid, header/footer heights)."""

    personality: OptionalNullable[Any] = UNSET
    """Brand personality traits (tone, energy, target audience)."""


class Branding1Dict(TypedDict):
    color_scheme: NotRequired[ColorSchemeOrStr]
    logo: NotRequired[str | None]
    colors: NotRequired[Colors | ColorsDict | None]
    fonts: NotRequired[list[Font | FontDict | None]]
    typography: NotRequired[Typography | TypographyDict | None]
    spacing: NotRequired[Spacing | SpacingDict | None]
    components: NotRequired[Components | ComponentsDict | None]
    icons: NotRequired[Any | None]
    images: NotRequired[Images2 | Images2Dict | None]
    animations: NotRequired[Any | None]
    layout: NotRequired[Any | None]
    personality: NotRequired[Any | None]
