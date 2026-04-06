from llm_wrapper import LLMWrapper
llm = LLMWrapper()
with open("strict_json.txt", "r") as f:
    template = f.read()

def extract(text):
    prompt = template.replace("{input}", text)
    return llm.generate(prompt, enforce_json=True)

texts = [
    "Rahul is a backend developer skilled in Node.js and MongoDB with 2 years experience.",
    "Priya is a frontend engineer using React.",
    "Amit works in HR."
]
for t in texts:
    print("\nInput:", t)
    print("Output:", extract(t))