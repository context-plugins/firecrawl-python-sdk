from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RedactPiientity(str, Enum):
    """Public PII entity buckets supported by Firecrawl redaction."""

    PERSON = "PERSON"
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    LOCATION = "LOCATION"
    FINANCIAL = "FINANCIAL"
    SECRET = "SECRET"

    __str__ = str.__str__


RedactPiientityOrStr: TypeAlias = Annotated[RedactPiientity | str, open_enum_validator(RedactPiientity)]
