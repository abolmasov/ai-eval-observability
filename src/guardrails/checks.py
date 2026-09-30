from __future__ import annotations

from dataclasses import dataclass
import re

PII_EMAIL = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
BLOCKLIST = ["ignore previous instructions", "exfiltrate", "disable safety"]


@dataclass
class GuardResult:
    allowed: bool
    reasons: list[str]


class GuardrailPipeline:
    def check_output(self, text: str) -> GuardResult:
        reasons: list[str] = []
        lowered = text.lower()
        if PII_EMAIL.search(text):
            reasons.append("pii_email")
        for term in BLOCKLIST:
            if term in lowered:
                reasons.append(f"policy:{term}")
        return GuardResult(allowed=not reasons, reasons=reasons)
