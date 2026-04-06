import time
import json
import logging
import os
from typing import Optional
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
load_dotenv()

#Logging setup
logging.basicConfig(
    filename="llm_output_logs.txt",
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
            timeout=30
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
                logging.info(f"Prompt: {prompt}")

                result = self.model.invoke(prompt)
                output = result.content.strip()
                logging.info(f"Raw output: {output}")
                #json enforcement
                if enforce_json:
                    output = self._ensure_json(output)
                return output
            except Exception as e:
                logging.error(f"Error: {str(e)}")
                if attempt < max_retries - 1:
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
                cleaned = text[start:end]
                json.loads(cleaned)
                return cleaned
            except:
                return "INVALID_JSON"
                