from langchain.memory import ConversationBufferWindowMemory

# ------------------ WINDOW MEMORY ------------------

window_memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    return_messages=True,

    # Keep only recent conversations
    k=4
)