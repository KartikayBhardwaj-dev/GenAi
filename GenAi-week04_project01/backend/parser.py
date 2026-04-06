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
        prompt = self.template.replace("{input}", text[:3000])

        for attempt in range(3):

            output = self.llm.generate(prompt, enforce_json=True)

            if output in ["FAILED", "INVALID_JSON"]:
                continue

            is_valid, error, data = validate_schema(output)

            if is_valid:
                return data   # ✅ return CLEAN JSON

            # 🔥 FEEDBACK LOOP (VERY IMPORTANT)
            prompt = prompt + f"""

The previous output was invalid due to:
{error}

Fix the JSON strictly.
Return ONLY valid JSON.
"""

        return {"error": "PARSING FAILED"}