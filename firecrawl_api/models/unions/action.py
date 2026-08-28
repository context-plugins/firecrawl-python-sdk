from __future__ import annotations

from typing import TypeAlias

from ..click import Click, ClickDict
from ..execute_java_script import ExecuteJavaScript, ExecuteJavaScriptDict
from ..generate_pdf import GeneratePdf, GeneratePdfDict
from ..press_a_key import PressAKey, PressAKeyDict
from ..scrape import Scrape, ScrapeDict
from ..screenshot1 import Screenshot1, Screenshot1Dict
from ..scroll import Scroll, ScrollDict
from ..write_text import WriteText, WriteTextDict
from .wait import Wait, WaitDict

Action: TypeAlias = (
    Wait | Screenshot1 | Click | WriteText | PressAKey | Scroll | Scrape | ExecuteJavaScript | GeneratePdf
)

ActionDict: TypeAlias = (
    WaitDict
    | Screenshot1Dict
    | ClickDict
    | WriteTextDict
    | PressAKeyDict
    | ScrollDict
    | ScrapeDict
    | ExecuteJavaScriptDict
    | GeneratePdfDict
)
