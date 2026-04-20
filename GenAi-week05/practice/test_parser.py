import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.output_parsers import ResponseSchema, StructuredOutputParser


load_dotenv()

# ✅ LLM
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    provider="groq",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

# ✅ Schema
schemas = [
    ResponseSchema(name="name", description="person name"),
    ResponseSchema(name="skills", description="list of skills as array"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)

# ✅ STRONG format instructions (override default)
format_instructions = """
Return ONLY valid JSON.

Rules:
- No markdown (no ```json)
- No explanation
- No thinking
- Use double quotes
- skills must be an array

Format:
{
  "name": "string",
  "skills": ["string"]
}
"""

# ✅ Prompt
prompt = PromptTemplate.from_template(
    """
Extract structured data from the text.

{format_instructions}

Text: {input}
"""
)

# ✅ Chain
chain = prompt | model

# ✅ Run
text = "Rahul is a Python developer skilled in FastAPI and MongoDB."

result = chain.invoke({
    "input": text,
    "format_instructions": format_instructions
})
raw = result.content if hasattr(result, "content") else result

print("RAW OUTPUT:\n", raw)




# ✅ CLEANING STEP (robust)
def clean_output(text: str) -> str:
    # remove thinking
    if "<think>" in text:
        text = text.split("</think>")[-1]

    # remove markdown
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            if "{" in part:
                text = part
                break

    # extract JSON
    start = text.find("{")
    end = text.rfind("}") + 1

    if start != -1 and end != -1:
        return text[start:end]

    return text


cleaned = clean_output(raw)

print("\nCLEANED:\n", cleaned)

# ✅ SAFE PARSE
try:
    parsed = parser.parse(cleaned)
    print("\nFINAL PARSED:\n", parsed)

except Exception as e:
    print("\n❌ Parsing failed")
    print(e)