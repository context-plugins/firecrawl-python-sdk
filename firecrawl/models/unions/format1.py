from __future__ import annotations

from typing import TypeAlias

from ..audio import Audio, AudioDict
from ..branding import Branding, BrandingDict
from ..change_tracking import ChangeTracking, ChangeTrackingDict
from ..highlights import Highlights, HighlightsDict
from ..html import Html, HtmlDict
from ..images import Images, ImagesDict
from ..json import Json, JsonDict
from ..links import Links, LinksDict
from ..markdown import Markdown, MarkdownDict
from ..menu import Menu, MenuDict
from ..product import Product, ProductDict
from ..question import Question, QuestionDict
from ..raw_html import RawHtml, RawHtmlDict
from ..screenshot import Screenshot, ScreenshotDict
from ..summary import Summary, SummaryDict
from ..video import Video, VideoDict

Format1: TypeAlias = (
    Markdown
    | Summary
    | Html
    | RawHtml
    | Links
    | Images
    | Screenshot
    | Json
    | ChangeTracking
    | Branding
    | Product
    | Menu
    | Audio
    | Video
    | Question
    | Highlights
)

Format1Dict: TypeAlias = (
    MarkdownDict
    | SummaryDict
    | HtmlDict
    | RawHtmlDict
    | LinksDict
    | ImagesDict
    | ScreenshotDict
    | JsonDict
    | ChangeTrackingDict
    | BrandingDict
    | ProductDict
    | MenuDict
    | AudioDict
    | VideoDict
    | QuestionDict
    | HighlightsDict
)
