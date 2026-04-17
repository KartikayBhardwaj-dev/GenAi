from llm_wrapper import LLMWrapper
from validator import validate_schema
import os
class ResumeParser:
    def __init__(self):
        self.llm = LLMWrapper()

        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "strict_json.txt")

        with open(file_path, "r") as f:
            self.template = f.read()

    def parse(self, text):
        print("Inside parser")

        prompt = self.template.replace("{input}", text[:1000])

        for attempt in range(3):
            print(f"Attempt {attempt+1} - calling LLM")

            output = self.llm.generate(prompt, enforce_json=True)

            print("LLM OUTPUT:", output)

            if output in ["FAILED", "INVALID_JSON"]:
                continue

            is_valid, error, data = validate_schema(output)

            if is_valid:
                print("VALID JSON FOUND")
                return data

            prompt = prompt + f"""
Previous output:
{output}

Error:
{error}

Fix the JSON.
"""

        return {"error": "PARSING FAILED"}