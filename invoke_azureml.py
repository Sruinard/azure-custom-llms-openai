import openai
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://localai-endpoint.swedencentral.inference.ml.azure.com"
model_path = "/v1/models"
completions_path = "/v1/chat/completions"



api_key = os.environ.get("AZURE_ML_DEPLOYMENT_KEY")
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'localai-deployment-phi-ds5' }

available_models = requests.get(base_url + model_path, headers=headers).json()["data"]

if available_models[0]["id"] != "phi-2":
    raise Exception("Model not found")
else:
    print("Model found")


import openai

# API key does not need to be valid
openai.base_url = base_url
openai.api_key = 'sk-XXXXXXXXXXXXXXXXXXXX'
openai.api_key = api_key


model_name = "phi-2"

completion = openai.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "Hi, how are you?",
        },
    ],
)
print(completion.choices[0].message.content)
