import logging
import os

# ---------- CREATE LOG DIRECTORY ----------

os.makedirs("logs", exist_ok=True)

# ---------- LOGGER CONFIG ----------

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)

# ---------- LOGGER ----------

logger = logging.getLogger(__name__)