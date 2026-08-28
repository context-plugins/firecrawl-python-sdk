from __future__ import annotations

from typing import TypeAlias

from ..html import Html, HtmlDict
from ..images import Images, ImagesDict
from ..json import Json, JsonDict
from ..links import Links, LinksDict
from ..markdown import Markdown, MarkdownDict
from ..raw_html import RawHtml, RawHtmlDict
from ..summary import Summary, SummaryDict

ParseFormats: TypeAlias = Markdown | Summary | Html | RawHtml | Links | Images | Json

ParseFormatsDict: TypeAlias = MarkdownDict | SummaryDict | HtmlDict | RawHtmlDict | LinksDict | ImagesDict | JsonDict
