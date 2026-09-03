from __future__ import annotations

from typing import TypeAlias

from ..images import Images, ImagesDict
from ..news import News, NewsDict
from ..web import Web, WebDict

Source1: TypeAlias = Web | Images | News

Source1Dict: TypeAlias = WebDict | ImagesDict | NewsDict
