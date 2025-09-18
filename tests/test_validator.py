from src.chatbot_guardrails.validator import Validator

def test_validator_stub():
    v = Validator()
    result = v.validate("What is AI?", "AI is artificial intelligence.")
    assert result["validated_response"] == "AI is artificial intelligence."
    assert result["is_hallucination"] is False
