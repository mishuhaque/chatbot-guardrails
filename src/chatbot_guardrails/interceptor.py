class Interceptor:
    """
    Intercepts chatbot responses before sending to the user.
    """

    def __init__(self):
        pass

    def intercept(self, query: str, response: str) -> dict:
        """
        Catch chatbot response and prepare it for validation.
        """
        return {"query": query, "response": response}
