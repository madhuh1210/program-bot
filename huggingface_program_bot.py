import requests
import os

API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

# Check if it's a Java-related question
def is_java_related(prompt: str):
    java_keywords = ["java", "jvm", "jdk", "jre", "spring boot"]
    return any(keyword in prompt.lower() for keyword in java_keywords)

# Send the prompt to Hugging Face
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

# Main chatbot loop
def main():
    print("Welcome to the Programming Helper (non-Java). Ask your question:\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        if is_java_related(user_input):
            print("Bot: Sorry, I cannot answer Java-related questions.\n")
            continue
        try:
            data = query({"inputs": user_input})
            generated_text = data[0]["generated_text"].replace(user_input, "").strip()
            print(f"Bot: {generated_text}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()



