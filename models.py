from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    model: str = "claude-opus-5"
    max_tokens: int = 16000
    system: str | None = None


class ChatResponse(BaseModel):
    content: str
    model: str
    stop_reason: str | None
    input_tokens: int
    output_tokens: int
