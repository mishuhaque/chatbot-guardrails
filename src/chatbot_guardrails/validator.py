class Validator:
    """
    Validates chatbot responses against retrieved documents.
    """

    def __init__(self):
        pass

    def validate(self, query: str, response: str, docs: list) -> dict:
        """
        Check if response aligns with supporting docs.
        (For MVP: simple keyword overlap; can extend with LLM judge.)
        """
        hallucination = True
        notes = "No supporting evidence found."

        for doc in docs:
            if any(word.lower() in doc.lower() for word in response.split()):
                hallucination = False
                notes = "Response aligns with supporting docs."
                break

        return {
            "validated_response": response,
            "is_hallucination": hallucination,
            "notes": notes
        }
