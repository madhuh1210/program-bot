import requests
import os
import random

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

# Generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Main chatbot loop with OTP
def main():
    print("Welcome to the Programming Helper (non-Java).")
    
    # OTP flow
    otp = generate_otp()
    print(f"\n🔐 Your OTP is: {otp}")
    user_input = input("Enter the OTP to continue: ")

    if user_input.strip() != otp:
        print("❌ Invalid OTP. Exiting.\n")
        return

    print("✅ OTP verified! Ask your programming question below:\n")

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



