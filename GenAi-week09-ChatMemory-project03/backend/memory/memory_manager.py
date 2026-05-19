from backend.memory.summary_memory import (
    summary_memory
)

# ------------------ GET MEMORY ------------------

def get_memory():

    return summary_memory

# ------------------ CLEAR MEMORY ------------------

def clear_memory():

    summary_memory.clear()