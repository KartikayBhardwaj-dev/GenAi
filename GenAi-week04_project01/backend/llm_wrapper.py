import time
import json
import logging
import os
from typing import Optional
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Logging setup
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/llm_output_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LLMWrapper:
    def __init__(self):
        api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

        self.llm = HuggingFaceEndpoint(
            repo_id="meta-llama/Llama-3.3-70B-Instruct",
            task="text-generation",
            provider="groq",
            huggingfacehub_api_token=api_token,
            timeout=30,
            temperature=0.3,          # ✅ control randomness
            max_new_tokens=500        # ✅ control length
        )

        self.model = ChatHuggingFace(llm=self.llm)

    def generate(
        self,
        prompt: str,
        max_retries: int = 3,
        delay: int = 2,
        enforce_json: bool = False,
    ) -> Optional[str]:

        for attempt in range(max_retries):
            try:
                logging.info(f"Attempt {attempt+1}")

                result = self.model.invoke(prompt)
                output = result.content.strip()

                logging.info(f"Raw output: {output[:500]}")  # ✅ limit log size

                # JSON enforcement
                if enforce_json:
                    output = self._ensure_json(output)

                    if output == "INVALID_JSON":
                        raise ValueError("Invalid JSON received")

                return output

            except Exception as e:
                logging.error(f"Error: {str(e)}")

                if attempt < max_retries - 1:

                    # 🔥 improve prompt on retry
                    prompt = prompt + f"""

The previous response was invalid.
Fix the output strictly.
Return ONLY valid JSON.
Attempt {attempt+2}/{max_retries}.
"""

                    time.sleep(delay * (attempt + 1))
                else:
                    return "FAILED"

    def _ensure_json(self, text: str) -> str:
        try:
            json.loads(text)
            return text

        except:
            try:
                start = text.find("{")
                end = text.rfind("}") + 1

                if start == -1 or end == -1:
                    return "INVALID_JSON"

                cleaned = text[start:end]

                json.loads(cleaned)
                return cleaned

            except:
                return "INVALID_JSON"