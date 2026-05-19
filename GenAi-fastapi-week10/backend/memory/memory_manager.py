from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

# ---------- SESSION STORAGE ----------

chat_sessions = {}

# ---------- GET SESSION ----------

def get_session(session_id):

    if session_id not in chat_sessions:

        chat_sessions[session_id] = {

            "history": [],

            "current_topic": None
        }

    return chat_sessions[session_id]

# ---------- CHAT HISTORY ----------

def get_chat_history(session_id):

    session = get_session(session_id)

    return session["history"]

# ---------- CURRENT TOPIC ----------

def get_current_topic(session_id):

    session = get_session(session_id)

    return session["current_topic"]

# ---------- SET CURRENT TOPIC ----------

def set_current_topic(
    session_id,
    topic
):

    session = get_session(session_id)

    session["current_topic"] = topic

# ---------- ADD USER MESSAGE ----------

def add_user_message(
    session_id,
    message
):

    history = get_chat_history(session_id)

    history.append(
        HumanMessage(content=message)
    )

# ---------- ADD AI MESSAGE ----------

def add_ai_message(
    session_id,
    message
):

    history = get_chat_history(session_id)

    history.append(
        AIMessage(content=message)
    )

# ---------- FORMAT HISTORY ----------

def format_chat_history(chat_history):

    history = []

    for message in chat_history:

        role = "User"

        if message.type == "ai":
            role = "Assistant"

        history.append(
            f"{role}: {message.content}"
        )

    return "\n".join(history)

# ---------- CLEAR HISTORY ----------

def clear_chat_history(session_id):

    if session_id in chat_sessions:

        chat_sessions[session_id] = {

            "history": [],

            "current_topic": None
        }