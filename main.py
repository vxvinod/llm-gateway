# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException

# from models import ChatRequest, ChatResponse
# from providers.anthropic_provider import AnthropicProvider

# load_dotenv()

# app = FastAPI(title="LLM Gateway")
# provider = AnthropicProvider()


# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest) -> ChatResponse:
#     try:
#         return provider.chat(
#             messages=request.messages,
#             model=request.model,
#             max_tokens=request.max_tokens,
#             system=request.system,
#         )
#     except RuntimeError as e:
#         raise HTTPException(status_code=502, detail=str(e))


# @app.get("/health")
# def health() -> dict[str, str]:
#     return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "gateway is alive"}

