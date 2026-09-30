from src.eval.harness import evaluate_answer
from src.guardrails.checks import GuardrailPipeline


def test_guard_blocks_email_pii():
    result = GuardrailPipeline().check_output("Contact me at person@example.com")
    assert result.allowed is False


def test_eval_scores_overlap():
    score = evaluate_answer(
        "refund window",
        "refund within 30 days",
        "refund within 30 days of purchase",
    )
    assert score.overall > 0
