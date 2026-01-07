from llm import load_llm
from langchain_core.messages import HumanMessage

llm = load_llm()
response = llm.invoke([HumanMessage(content="Explain LLMs in simple terms")])
print(response.content)
