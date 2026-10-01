import anthropic

from models import ChatMessage, ChatResponse


class AnthropicProvider:
    def __init__(self) -> None:
        self.client = anthropic.Anthropic()

    def chat(
        self,
        messages: list[ChatMessage],
        model: str,
        max_tokens: int,
        system: str | None = None,
    ) -> ChatResponse:
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": m.role, "content": m.content} for m in messages],
            )
        except anthropic.AuthenticationError as e:
            raise RuntimeError("Invalid Anthropic API key") from e
        except anthropic.RateLimitError as e:
            raise RuntimeError("Rate limited by Anthropic API") from e
        except anthropic.APIStatusError as e:
            raise RuntimeError(f"Anthropic API error: {e.message}") from e
        except anthropic.APIConnectionError as e:
            raise RuntimeError("Could not connect to Anthropic API") from e

        text = next((b.text for b in response.content if b.type == "text"), "")

        return ChatResponse(
            content=text,
            model=response.model,
            stop_reason=response.stop_reason,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )
