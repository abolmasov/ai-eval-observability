from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EvalScore:
    relevance: float
    faithfulness: float
    overall: float


def _overlap(a: str, b: str) -> float:
    sa, sb = set(a.lower().split()), set(b.lower().split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def evaluate_answer(question: str, answer: str, context: str) -> EvalScore:
    relevance = _overlap(question, answer)
    faithfulness = _overlap(answer, context)
    overall = round((relevance + faithfulness) / 2, 3)
    return EvalScore(relevance=round(relevance, 3), faithfulness=round(faithfulness, 3), overall=overall)
