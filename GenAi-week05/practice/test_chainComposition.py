import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    provider="groq",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

# EXCTRACTION PROMPT

extract_prompt = PromptTemplate.from_template(
    """
Extract structured data from the text.
Return ONLY JSON.
Format:
{{
  "name": "string",
  "skills": ["string"],
  "experience": "string"
}}
Text:
{input}
"""
)

def clean_output(text: str) -> str:
    if "<think>" in text:
        text = text.split("</think>")[-1]
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            if "{" in part:
                text = part
                break
    start = text.find("{")
    end = text.rfind("}") + 1
    if start != -1 and end != -1:
        return text[start:end]
    return text

cleaner = RunnableLambda(lambda x: clean_output(x.content))

summary_prompt = PromptTemplate.from_template(
    """
Convert the following JSON into a clean professional sentence.
JSON:
{data}
Output:
"""
)

# TRANSFORM JSON -> STRING

to_summary_input = RunnableLambda(
    lambda x: {"data", x}
)

# FULL CHAIN COMPOSITION

chain = (
    extract_prompt
    | model
    | cleaner
    | to_summary_input
    | summary_prompt
    | model
)

text = """
Rahul Sharma is a backend developer.
He has worked with:
- Python
- FastAPI
- MongoDB
He has around 2 years of experience.
"""

result = chain.invoke({"input": text})
output = result.content if hasattr(result, "content") else result
print("\nFINAL OUTPUT:\n")
print(output)

