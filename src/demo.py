from src.eval.harness import evaluate_answer
from src.guardrails.checks import GuardrailPipeline
from src.tracing.tracer import Tracer


def main() -> None:
    tracer = Tracer()
    tracer.span("demo_start")
    guards = GuardrailPipeline()
    text = "Refunds are available within 30 days."
    g = guards.check_output(text)
    score = evaluate_answer(
        "What is the refund window?",
        text,
        "Refunds are available within 30 days of purchase.",
    )
    tracer.span("demo_end", allowed=g.allowed, overall=score.overall)
    print({"trace_id": tracer.trace_id, "guard": g, "score": score})


if __name__ == "__main__":
    main()
