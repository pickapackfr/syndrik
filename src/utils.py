from llama_index.core.llms import ChatMessage, MessageRole

def convert_to_chat_messages(messages):
    """Convertit les messages Streamlit en ChatMessage LlamaIndex"""
    chat_messages = []
    for msg in messages:
        role_map = {
            "system": MessageRole.SYSTEM,
            "user": MessageRole.USER,
            "assistant": MessageRole.ASSISTANT
        }
        chat_messages.append(
            ChatMessage(role=role_map[msg["role"]], content=msg["content"])
        )
    return chat_messages