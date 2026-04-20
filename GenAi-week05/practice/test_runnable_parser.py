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

response_schema = [
    ResponseSchema(name="name", description="person name"),
    ResponseSchema(name="skills", description="list of skills as array")
]

parser = StructuredOutputParser.from_response_schemas(response_schema)

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


prompt = PromptTemplate.from_template(
    """
Extract structured data from the text.

{format_instructions}

Text: {input}
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

chain = prompt | model  | cleaner | parser

# text = "Rahul is a Python developer skilled in FastAPI and MongoDB."
# text = "Rahul Sharma is a backend engineer with 2 years experience in Python, FastAPI, MongoDB. Also worked with Docker."

# text = "Resume: Rahul Sharma\nSkills: Python, FastAPI\nExperience: 2 years"

# text = """
# Rahul Sharma is a backend developer.

# He has worked with:
# - Python
# - FastAPI
# - MongoDB

# He has around 2 years of experience.
# """

text = """
RESUME

Name: Rahul Sharma

Skills:
Python, FastAPI, MongoDB, Docker

Experience:
Worked at XYZ company for 2 years.

Projects:
- Built APIs
- Worked on backend systems

Contact: rahul@email.com
"""
result = chain.invoke({
    "input": text,
    "format_instructions": format_instructions
})

print(result)