from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if api_key:
        print("DeepSeek API Key Loaded Successfully!")
    else:
        print("Failed to Load DeepSeek API Key. Check .env file.")

if __name__ == "__main__":
    main()
