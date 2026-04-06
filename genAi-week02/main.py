from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="text-generation",
    provider="groq"
)

model = ChatHuggingFace(llm=llm)


zero_shot_file_path = "/Users/kartikaybhardwaj/Desktop/genAi-week02/zero_shot.txt"
with open(zero_shot_file_path, "r") as f:
    template = f.read()


few_shot_file_path = "/Users/kartikaybhardwaj/Desktop/genAi-week02/few_shot.txt"
with open(few_shot_file_path, "r") as f:
    template1 = f.read()

strict_json_file_path = "/Users/kartikaybhardwaj/Desktop/genAi-week02/strict_json_generator.txt"
with open(strict_json_file_path, "r") as f:
    template2 = f.read()
def extract(text):
    prompt = template2.replace("{input}", text)

    result = model.invoke(prompt)
    return result.content
texts = [
    "Rahul is a backend developer skilled in Node.js and MongoDB with 2 years experience.",
    "Priya is a frontend engineer using React.",
    "Amit works in HR."
]

for t in texts:
    print("\nInput:", t)
    print("Output:\n", extract(t))