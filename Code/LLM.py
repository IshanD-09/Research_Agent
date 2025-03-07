from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def summarize():
    template = """Give me a list of key facts about this paper {paper}"""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3.2")

    retrieved_documents = retriever.invoke(template)

    chain = prompt | model

    print(chain.invoke({"paper": retrieved_documents}))