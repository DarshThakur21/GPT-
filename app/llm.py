# import os
# from langchain_huggingface import HuggingFaceEndpoint

# def load_llm():
#     return HuggingFaceEndpoint(
#         repo_id="google/flan-t5-base",
#         task="text-generation",
#         temperature=0.2,
#         max_new_tokens=256,
#         huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     )

import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

def load_llm():
    endpoint = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="conversational",
        max_new_tokens=256,
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )
    return ChatHuggingFace(llm=endpoint)
