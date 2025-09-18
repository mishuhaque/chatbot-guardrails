from fastapi import FastAPI
from pydantic import BaseModel

from .interceptor import Interceptor
from .validator import Validator
from .retriever import Retriever
from .formatter import Formatter

app = FastAPI(title="Chatbot Guardrails API")

# Initialize components
interceptor = Interceptor()
retriever = Retriever()
validator = Validator()
formatter = Formatter()

class ChatRequest(BaseModel):
    query: str
    response: str

@app.post("/improve")
async def improve_chat(request: ChatRequest):
    intercepted = interceptor.intercept(request.query, request.response)
    docs = retriever.retrieve(request.query)
    validated = validator.validate(intercepted["query"], intercepted["response"], docs)
    final_output = formatter.format(
        intercepted["query"],
        validated["validated_response"],
        docs,
        validated["is_hallucination"],
        validated["notes"]
    )
    return {
        "improved_response": final_output.strip(),
        "hallucination": validated["is_hallucination"],
        "notes": validated["notes"],
        "docs": docs
    }
