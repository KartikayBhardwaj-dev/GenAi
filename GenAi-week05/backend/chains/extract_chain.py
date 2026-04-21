import os
import time
import logging
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from validators.validator import validate_and_clean

load_dotenv()

# ------------------ LOGGING ------------------
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/extraction_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------ MODEL ------------------
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    provider="groq",
    temperature=0.2,
    max_new_tokens=200,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

# ------------------ PROMPT ------------------
file_path = "/Users/kartikaybhardwaj/Desktop/GenAi/GenAi-week05/backend/prompts/extract_prompt.txt"

with open(file_path, "r") as f:
    template = f.read()

prompt = PromptTemplate.from_template(template)

# ------------------ CLEANER ------------------
def clean_output(text: str) -> str:
    # Remove thinking traces
    if "<think>" in text:
        text = text.split("</think>")[-1]

    # Remove markdown blocks
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            if "{" in part:
                text = part
                break

    # Extract JSON
    start = text.find("{")
    end = text.rfind("}") + 1

    if start != -1 and end != -1:
        return text[start:end]

    return text

cleaner = RunnableLambda(
    lambda x: clean_output(x.content if hasattr(x, "content") else x)
)

# ------------------ VALIDATOR ------------------
def validate_step(text: str):
    is_valid, error, data = validate_and_clean(text)

    if not is_valid:
        raise ValueError(error)

    return data

validator = RunnableLambda(validate_step)

# ------------------ CHAIN ------------------
chain = prompt | model | cleaner | validator

# ------------------ RETRY LOGIC ------------------
def run_with_retry(chain, input_text, max_retries=3):
    base_input = {
        "input": input_text,
        "feedback": ""
    }

    last_error = None

    for attempt in range(max_retries):
        try:
            logging.info(f"Attempt {attempt+1}")

            result = chain.invoke(base_input)

            logging.info(f"SUCCESS: {result}")
            return {
                "success": True,
                "data": result,
                "error": None
            }

        except Exception as e:
            last_error = str(e)

            logging.error(f"Attempt {attempt+1} failed: {last_error}")

            # Add feedback separately (important fix)
            base_input["feedback"] = f"""
Previous output was invalid due to:
{last_error}

Fix the JSON strictly.
Return ONLY valid JSON.
"""

            time.sleep(1 * (attempt + 1))

    return {
        "success": False,
        "data": None,
        "error": f"Failed after {max_retries} attempts: {last_error}"
    }

# ------------------ TEST ------------------
if __name__ == "__main__":
    text = """
    Rahul Sharma is a backend developer.

    He has worked with:
    - Python
    - FastAPI
    - MongoDB

    He has around 2 years of experience.
    """

    result = run_with_retry(chain, text)

    print(result)