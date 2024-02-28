import os
import dataclasses

import openai
from dotenv import load_dotenv


@dataclasses.dataclass
class ChatConfig:
    base_url: str
    model_name: str
    api_key: str


def load_config() -> ChatConfig:
    base_url = os.environ.get("AZURE_ML_BASE_URL")
    model_name = os.environ.get("AZURE_ML_MODEL_NAME")
    api_key = os.environ.get("AZURE_ML_DEPLOYMENT_KEY")

    return ChatConfig(base_url=base_url, model_name=model_name, api_key=api_key)


class AzureMLChat:
    def __init__(self, cfg: ChatConfig):
        self.cfg = cfg
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cfg.api_key}",
        }
        openai.base_url = cfg.base_url
        openai.api_key = cfg.api_key

    def invoke(self, user_input: str) -> str:
        completion = openai.chat.completions.create(
            model=self.cfg.model_name,
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )
        return completion.choices[0].message.content


if __name__ == "__main__":
    print("Loading config...")
    load_dotenv()
    cfg = load_config()
    print("Done.")

    print("Invoking AzureML...")
    chat = AzureMLChat(cfg)
    user_input = "Tell me something about Azure Machine Learning"
    response = chat.invoke(user_input=user_input)
    print(user_input, "=>", response)
