# from langchain_core.messages import (HumanMessage, AIMessage)

# # -----------------CHAT HISTORY-----------------
# chat_history = []

# # -----------ADD USER MESSAGE-----------------
# def add_user_message(message):
#     chat_history.append(
#         HumanMessage(content=message)
#     )

# # -----------------ADD AI MESSAGE--------------
# def add_ai_message(message):
#     chat_history.append(
#         AIMessage(content=message)
#     )

# # GET CHAT HISTORY
# def get_chat_history():
#     return chat_history


from langchain.memory import ConversationBufferMemory

# ------------------ BUFFER MEMORY ------------------

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)