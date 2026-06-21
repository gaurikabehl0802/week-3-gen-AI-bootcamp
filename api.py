import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
print(API_TOKEN)

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def generate_image(prompt):

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt},
        timeout=60
    )

    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Text:", response.text[:500])

    return response