from __future__ import annotations

from typing import TypeAlias

from ..git_hub import GitHub, GitHubDict
from ..pdf import Pdf, PdfDict
from ..research import Research, ResearchDict

Category: TypeAlias = GitHub | Research | Pdf

CategoryDict: TypeAlias = GitHubDict | ResearchDict | PdfDict
