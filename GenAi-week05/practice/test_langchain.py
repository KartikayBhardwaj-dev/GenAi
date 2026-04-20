import os 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
load_dotenv()

llm =  HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation",
    provider="groq",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate.from_template("Explain {Topic} in one line")
chain = prompt | model
result = chain.invoke({"Topic": "Running"})
print(result.content)
