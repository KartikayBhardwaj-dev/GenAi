sessions = {}

# -----------CREATE SESSIONS-------
def create_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "vectorstore": None,
            "metadata": {}
        }

    return sessions[session_id]

# ---------SET VECTORSTORE------------
def set_vectorstore(session_id, vectorstore):
    session = create_session(session_id)
    session["vectorstore"] = vectorstore

# -------GET VECTORSTORE----------
def get_vectorstore(session_id):
    session = create_session(session_id)
    return session.get("vectorstore")

# -----------SESSION EXISTS--------
def session_exists(session_id):
    return session_id in sessions

# -----------DELETE SESSIONS-----------
def delete_session(session_id):
    if session_id in sessions:
        del sessions[session_id]

# --------GET ALL SESSIONS-------
def get_all_sessions():
    return sessions