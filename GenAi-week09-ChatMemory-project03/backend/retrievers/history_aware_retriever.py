from backend.chains.chat_chain import chat_chain

# --------CREATE STANDALONE QUESTION-----------
def generate_standalone_question(question, chat_history):
    history_text = ""
    for message in chat_history:
        history_text += f"{message.type}: {message.content}\n"

    standalone_question = chat_chain.invoke({
        "chat_history": history_text,
        "question": question
    })
    return standalone_question