from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import uuid


@dataclass
class Span:
    name: str
    attributes: dict[str, Any]
    ts: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class Tracer:
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    spans: list[Span] = field(default_factory=list)

    def span(self, name: str, **attributes: Any) -> None:
        self.spans.append(Span(name=name, attributes=attributes))
