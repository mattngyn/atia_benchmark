import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables!")

print(f"Using API key: {api_key[:10]}...")

client = genai.Client(api_key=api_key)

print("Uploading video file...")
myfile = client.files.upload(file="2fa_attack_2x.mp4")
print(f"File uploaded: {myfile.name}")

print("Waiting for file to be processed...")
max_attempts = 12  
attempts = 0

while myfile.state.name == "PROCESSING" and attempts < max_attempts:
    print(".", end="", flush=True)
    time.sleep(10)
    attempts += 1

    file_list = client.files.list()
    for f in file_list:
        if f.name == myfile.name:
            myfile = f
            break

if myfile.state.name == "FAILED":
    raise ValueError(f"File processing failed: {myfile.state}")
elif myfile.state.name == "PROCESSING":
    print(f"\nFile is still processing after {max_attempts * 10} seconds. Trying anyway...")
else:
    print(f"\nFile is ready: {myfile.state.name}")

print("Generating content...")
response = client.models.generate_content(
    model="gemini-2.0-flash-exp", 
    contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print("\n" + "="*50)
print("RESPONSE:")
print("="*50)
print(response.text)
