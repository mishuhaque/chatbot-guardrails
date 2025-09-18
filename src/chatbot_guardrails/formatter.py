class Formatter:
    """
    Formats improved responses with citations and hallucination warnings.
    """

    def __init__(self):
        pass

    def format(self, query: str, response: str, docs: list, hallucination: bool, notes: str) -> str:
        disclaimer = "⚠️ This answer may be a hallucination." if hallucination else ""
        docs_text = "\n".join([f"- {doc}" for doc in docs])
        return f"""
User asked: {query}

Chatbot answered: {response}

{disclaimer}
Notes: {notes}

Supporting docs:
{docs_text}
"""
